class Persona:
   

    def __init__(self, nome, cognome):
        # ATTRIBUTI PRIVATI: il doppio underscore (__) li "nasconde"
        self.__nome = nome
        self.__cognome = cognome

    # --- METODI GETTER (le "chiavi" per leggere i dati) ---
   
    def get_nome(self):
        """Restituisce il nome."""
        return self.__nome

    def get_cognome(self):
        """Restituisce il cognome."""
        return self.__cognome

    # --- METODI SETTER

    def set_nome(self, nuovo_nome):
        """Modifica il nome, ma solo se non è vuoto."""
        if nuovo_nome != "":
            self.__nome = nuovo_nome
            print(f"Nome modificato in: {nuovo_nome}")
        else:
            print("Errore: il nome non può essere vuoto!")
           
    # --- Altri metodi pubblici ---
   
    def saluta(self):
       
        # Usa i metodi 'get' per accedere ai dati in modo sicuro
        print(f"Ciao! Mi chiamo {self.get_nome()} {self.get_cognome()}.")


# === ESEMPIO DI UTILIZZO ===

# 1. Creiamo un oggetto Persona
persona1 = Persona("Mario", "Rossi")
persona1.saluta()

print("-" * 20)

# 2. PROVA SBAGLIATA: cerco di accedere direttamente al nome
try:
    print(persona1.__nome)
except AttributeError:
    print("Non posso accedere a '__nome' direttamente!")

print("-" * 20)

# 3. MODO CORRETTO: uso i metodi 'get' e 'set'

print(f"Il nome attuale è: {persona1.get_nome()}")

# Modifico il nome con un valore valido
persona1.set_nome("Luigi")

# Provo a modificarlo con un valore non valido
persona1.set_nome("")

# Vediamo il risultato finale
persona1.saluta()
