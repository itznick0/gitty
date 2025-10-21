import pickle
import os
import random
from datetime import datetime

# Cambia la working directory alla cartella dello script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Costanti per i nomi dei file
UTENTI_FILE = "utenti.pkl"


# Classe Transaction (inalterata)
class Transaction:
    def __init__(self, timestamp="N/A", operation_type="N/A", amount=0, balance_after=0):
        self.timestamp = timestamp
        self.operation_type = operation_type
        self.amount = amount
        self.balance_after = balance_after

    def __str__(self):
        return f"[{self.timestamp}] {self.operation_type}: {self.amount:.2f} EUR | Balance: {self.balance_after:.2f} EUR"


# Classe BankAccount (senza IBAN random ogni volta: lo salveremo!)
class BankAccount:
    def __init__(self, iban=None):
        self.iban = iban if iban is not None else random.randint(10**10, 10**11 - 1)
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction = Transaction(
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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

    def save_to_file(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load_from_file(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)


# Classe DebitCard (ora separata dal conto)
class DebitCard:
    def __init__(self, card_number=None, pin=None):
        self.card_number = card_number if card_number is not None else random.randint(10**15, 10**16 - 1)
        self.pin = pin if pin is not None else random.randint(10**4, 10**5 - 1)
        # Il conto NON è più qui: sarà caricato separatamente

    def verify_pin(self, entered_pin):
        return entered_pin == self.pin


# Classe Customer (ora solo dati identificativi + carta)
class Customer:
    def __init__(self, first_name, last_name, card=None):
        self.first_name = first_name
        self.last_name = last_name
        self.card = card if card is not None else DebitCard()

    def get_account_filename(self):
        return f"user_{self.card.card_number}.pkl"

    def load_account(self):
        filename = self.get_account_filename()
        if os.path.isfile(filename):
            return BankAccount.load_from_file(filename)
        else:
            # Crea un nuovo conto se non esiste
            account = BankAccount()
            account.save_to_file(filename)
            return account

    def save_account(self, account):
        filename = self.get_account_filename()
        account.save_to_file(filename)


# Funzioni per gestire la lista globale degli utenti
def load_all_customers():
    if os.path.isfile(UTENTI_FILE):
        with open(UTENTI_FILE, "rb") as f:
            return pickle.load(f)
    return []

def save_all_customers(customers):
    with open(UTENTI_FILE, "wb") as f:
        pickle.dump(customers, f)


# Helper input
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


# Funzione principale
def main_console():
    # Carica tutti gli utenti registrati
    customers = load_all_customers()

    # Se è la prima esecuzione, crea 2 utenti di esempio
    if not customers:
        print("No users found. Creating 2 example customers...")
        cust1 = Customer("Mario", "Rossi")
        cust2 = Customer("Luigi", "Bianchi")
        customers = [cust1, cust2]
        save_all_customers(customers)

        # Salva i loro conti vuoti
        for c in customers:
            account = BankAccount()
            c.save_account(account)

        print(f"Customer 1 - Card: {cust1.card.card_number}, PIN: {cust1.card.pin}")
        print(f"Customer 2 - Card: {cust2.card.card_number}, PIN: {cust2.card.pin}")

    # Login
    logged_in_customer = None
    while True:
        print("\n=== ATM LOGIN ===")
        try:
            card_number = get_integer_input("Enter your card number: ")
            pin = get_integer_input("Enter your PIN: ")
        except KeyboardInterrupt:
            print("\nForced exit.")
            return

        for customer in customers:
            if customer.card.card_number == card_number:
                if customer.card.verify_pin(pin):
                    logged_in_customer = customer
                    break
                else:
                    break  # carta trovata ma PIN sbagliato

        if logged_in_customer:
            print(f"\nWelcome, {logged_in_customer.first_name} {logged_in_customer.last_name}!")
            break
        else:
            print("Invalid card number or PIN. Please try again.")

    # Carica il conto dell'utente
    account = logged_in_customer.load_account()

    # Menu principale
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Check balance")
        print("2. Withdraw money")
        print("3. Deposit money")
        print("4. View transaction history")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print(f"Current balance: {account.get_balance():.2f} EUR")

        elif choice == "2":
            amount = get_float_input("Enter amount to withdraw: ")
            account.withdraw(amount)
            logged_in_customer.save_account(account)  # Salva subito

        elif choice == "3":
            amount = get_float_input("Enter amount to deposit: ")
            account.deposit(amount)
            logged_in_customer.save_account(account)  # Salva subito

        elif choice == "4":
            transactions = account.get_transactions()
            if transactions:
                print("\n=== TRANSACTION HISTORY ===")
                for t in transactions:
                    print(t)
            else:
                print("No transactions found.")

        elif choice == "5":
            logged_in_customer.save_account(account)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# Avvio diretto
try:
    main_console()
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
except Exception as e:
    print(f"Unexpected error: {e}")