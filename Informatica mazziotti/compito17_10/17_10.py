import pickle
import os
import random
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Classes
class Transaction:
    def __init__(self, timestamp="N/A", operation_type="N/A", amount=0, balance_after=0):
        self.timestamp = timestamp
        self.operation_type = operation_type
        self.amount = amount
        self.balance_after = balance_after

    def __str__(self):
        return f"[{self.timestamp}] {self.operation_type}: {self.amount:.2f} EUR | Balance: {self.balance_after:.2f} EUR"


class BankAccount:
    def __init__(self):
        self.iban = random.randint(10**10, 10**11 - 1)
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction = Transaction(
                datetime.now().strftime("%A, %d %B %Y -- %H:%M:%S"),
                "Deposit",
                amount,
                self.balance
            )
            self.transactions.append(transaction)
            print(f"Deposit of {amount:.2f} EUR completed.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            transaction = Transaction(
                datetime.now().strftime("%A, %d %B %Y -- %H:%M:%S"),
                "Withdrawal",
                amount,
                self.balance
            )
            self.transactions.append(transaction)
            print(f"Withdrawal of {amount:.2f} EUR completed.")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions


class DebitCard:
    def __init__(self):
        self.card_number = random.randint(10**15, 10**16 - 1)
        self.pin = random.randint(10**4, 10**5 - 1)
        self.linked_account = BankAccount()

    def verify_pin(self, entered_pin):
        return entered_pin == self.pin


class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.card = DebitCard()


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def find_customer_by_card(self, card_number):
        for customer in self.customers:
            if customer.card.card_number == card_number:
                return customer
        return None

    def save_data(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    def load_data(self, filename):
        with open(filename, "rb") as f:
            loaded = pickle.load(f)
            self.customers = loaded.customers
            self.bank_name = loaded.bank_name


# Helper functions for safe input
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


# Main console application
def main_console():
    global bank
    data_file = "bank_data.pkl"

    # Load or initialize bank
    if os.path.isfile(data_file):
        try:
            bank = Bank("")
            bank.load_data(data_file)
            print("Data loaded successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")
            print("Creating a new bank...")
            bank = Bank("Octopus Bank")
    else:
        bank = Bank("Octopus Bank")
        # Add example customers (only once)
        cust1 = Customer("Mario", "Rossi")
        cust2 = Customer("Luigi", "Bianchi")
        bank.add_customer(cust1)
        bank.add_customer(cust2)
        bank.save_data(data_file)
        print("Bank initialized with 2 example customers.")
        print(f"Customer 1 - Card: {cust1.card.card_number}, PIN: {cust1.card.pin}")
        print(f"Customer 2 - Card: {cust2.card.card_number}, PIN: {cust2.card.pin}")

    # Login loop
    while True:
        print("\n=== ATM LOGIN ===")
        try:
            card_number = get_integer_input("Enter your card number: ")
            pin = get_integer_input("Enter your PIN: ")
        except KeyboardInterrupt:
            print("\nForced exit.")
            return

        customer = bank.find_customer_by_card(card_number)
        if customer and customer.card.verify_pin(pin):
            print(f"\nWelcome, {customer.first_name} {customer.last_name}!")
            break
        else:
            print("Invalid card number or PIN. Please try again.")

    # Main menu
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Check balance")
        print("2. Withdraw money")
        print("3. Deposit money")
        print("4. View transaction history")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print(f"Current balance: {customer.card.linked_account.get_balance():.2f} EUR")

        elif choice == "2":
            amount = get_float_input("Enter amount to withdraw: ")
            customer.card.linked_account.withdraw(amount)

        elif choice == "3":
            amount = get_float_input("Enter amount to deposit: ")
            customer.card.linked_account.deposit(amount)

        elif choice == "4":
            transactions = customer.card.linked_account.get_transactions()
            if transactions:
                print("\n=== TRANSACTION HISTORY ===")
                for t in transactions:
                    print(t)
            else:
                print("No transactions found.")

        elif choice == "5":
            bank.save_data(data_file)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
