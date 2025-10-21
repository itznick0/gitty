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
try:
    classe_richiesta = input("Inserire la classe per la quale generare la comunicazione: ").strip().upper()
    cartella = classe_richiesta
    nome_file_pkl = cartella + "\\biglietti_" + classe_richiesta + ".pkl"
    nome_file_txt = cartella + "\\comunicazione_" + classe_richiesta + ".txt"
    with open(nome_file_pkl, "rb") as f:
        studenti = pickle.load(f)
    with open("compito24_09-4.txt", "r") as f_modello:
        modello = f_modello.read()
    elenco_studenti = ""
    totale = 0.0
    for s in studenti:
        nome_str = s.nome
        spazi_nome = " " * (35 - len(nome_str))
        cognome_str = s.cognome
        spazi_cognome = " " * (15 - len(cognome_str))
        eta_str = str(s.eta)
        spazi_eta = " " * (10 - len(eta_str))
        prezzo_str = f"{s.prezzo:.2f}"
        spazi_prezzo = " " * (10 - len(prezzo_str))
        riga = nome_str + spazi_nome + cognome_str + spazi_cognome + eta_str + spazi_eta + "Euro " + prezzo_str + spazi_prezzo
        elenco_studenti += riga + "\n"
        totale += s.prezzo
    comunicazione = modello.replace("{CLASSE}", classe_richiesta)
    comunicazione = comunicazione.replace("{ELENCO_STUDENTI}", elenco_studenti.rstrip())
    comunicazione = comunicazione.replace("{TOTALE}", f"{totale:.2f}")
    with open(nome_file_txt, "w") as f_output:
        f_output.write(comunicazione)
    print(f"File {nome_file_txt} creato con successo.")
except FileNotFoundError as e:
    print(f"Errore: File non trovato. Dettagli: {e}")
except IOError as e:
    print(f"Errore di I/O: Impossibile scrivere sul file. Dettagli: {e}")
except Exception as e:
    print(f"Si è verificato un errore inaspettato: {e}")
