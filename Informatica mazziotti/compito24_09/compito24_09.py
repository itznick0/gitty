import os
from dataclasses import dataclass
import pickle
os.chdir(os.path.dirname(os.path.abspath(__file__)))
@dataclass
class StudentePagante:
    nome: str
    cognome: str
    eta: int
    prezzo: float

#Sezione P mancante (non trovata negli elenchi)

try:
    classe_richiesta = input("Inserire una classe (sezione P non presente): ").strip().upper()
    with open("compito24_09-3.txt", "r") as indice:
        posizione = None
        for riga in indice.readlines():
            if riga.startswith(classe_richiesta + "-"):
                posizione = int(riga.split("-")[1])
    while posizione is None:
        print(f"Classe {classe_richiesta} non trovata nell'indice.")
        classe_richiesta = input("Inserire una classe: ").strip().upper()
        with open("compito24_09-3.txt", "r") as indice:
            posizione = None
            for riga in indice.readlines():
                if riga.startswith(classe_richiesta + "-"):
                    posizione = int(riga.split("-")[1])
    else:
        with open("compito24_09-2.txt", "r") as elenco:
            elenco.seek(posizione)
            riga_classe = elenco.readline()
            studenti = []
            riga_studente = elenco.readline().strip()
            while riga_studente and not (riga_studente[0].isdigit() and " " not in riga_studente.split()[0]):
                parti = riga_studente.split()
                if len(parti) >= 3:
                    eta = int(parti[-1])
                    cognome = parti[0]
                    nome = ""
                    for i in range(1, len(parti) - 1): 
                        if i > 1:
                            nome += " " 
                        nome += parti[i]
                    if eta < 18:
                        prezzo = 6.0
                    else:
                        prezzo = 8.0
                    studenti.append(StudentePagante(nome, cognome, eta, prezzo))
                riga_studente = elenco.readline().strip()
        cartella = classe_richiesta
        if not os.path.isdir(cartella):
            os.mkdir(cartella)
        nome_file_pkl = cartella + "\\biglietti_" + classe_richiesta + ".pkl"
        with open(nome_file_pkl, "wb") as f:
            pickle.dump(studenti, f)
        print(f"File {nome_file_pkl} creato con successo.")
except FileNotFoundError as e:
    print(f"Errore: File non trovato. Dettagli: {e}")
except IOError as e:
    print(f"Errore di I/O: Impossibile scrivere sul file. Dettagli: {e}")
except Exception as e:
    print(f"Si è verificato un errore inaspettato: {e}")