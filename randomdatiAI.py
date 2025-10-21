import random

# Lista di nomi e cognomi casuali
nomi = ["Mario", "Luigi", "Giuseppe", "Francesco", "Antonio", "Marco", "Andrea", "Paolo", "Giovanni", "Matteo", 
        "Alessandro", "Roberto", "Stefano", "Davide", "Luca", "Federico", "Simone", "Giorgio", "Michele", "Alessio",
        "Elena", "Maria", "Anna", "Sofia", "Giulia", "Martina", "Francesca", "Chiara", "Valentina", "Eleonora",
        "Laura", "Silvia", "Veronica", "Cristina", "Elisa", "Roberta", "Monica", "Patrizia", "Gianna", "Lucia"]

cognomi = ["Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Ricci", "Marino", "Greco",
           "Bruno", "Gallo", "Conti", "De Luca", "Mancini", "Costa", "Giordano", "Lombardi", "Moretti", "Barbieri",
           "Fontana", "Santoro", "Mariani", "Rinaldi", "Caruso", "Ferrara", "Galli", "Martini", "Leone", "Longo",
           "Vitale", "Conte", "Ferri", "Pellegrini", "Serra", "Coppola", "Bianco", "Palmieri", "D'Angelo", "Moro"]

# Genero il file CSV con 50 studenti casuali
with open("studenti.csv", "w", encoding="utf-8") as file:
    for i in range(50):
        matricola = f"S{i+1:03d}"  # Formatta la matricola come S001, S002, ecc.
        nome = random.choice(nomi)
        cognome = random.choice(cognomi)
        # Genero voti casuali per simulare il formato richiesto (anche se non usati nel codice principale)
        
        file.write(f"{matricola},{nome},{cognome}\n")

print("File studenti.csv creato con successo!")