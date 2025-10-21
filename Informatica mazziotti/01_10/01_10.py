import pickle
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Studente:
    def __init__(self, matricola, nome, cognome):
        self.__matricola = matricola
        self.__nome = nome
        self.__cognome = cognome

    def get_matricola(self):
        return self.__matricola

    def get_nome(self):
        return self.__nome

    def get_cognome(self):
        return self.__cognome

    def __str__(self):
        return f"Matricola: {self.__matricola}, Nome: {self.__nome}, Cognome: {self.__cognome}"


def crea_file_studenti():
    # Apro il file indice in modalità "w" per svuotarlo e ricrearlo
    with open("indice.txt", "w", encoding="utf-8") as file_indice:
        with open("studenti.csv", "r", encoding="utf-8") as file_csv:
            for riga in file_csv:
                riga = riga.strip()
                if riga:
                    parti = riga.split(',')
                    if len(parti) >= 3:
                        matricola = parti[0]
                        nome = parti[1]
                        cognome = parti[2]
                        
                        # Creo l'oggetto Studente
                        studente = Studente(matricola, nome, cognome)
                        with open("studenti.dat", "ab") as file_bin:
                            posizione = file_bin.tell()
                            pickle.dump(studente, file_bin)
                        file_indice.write(f"{matricola},{posizione}\n")


def cerca_studente_per_matricola(matricola_da_cercare):
    posizione = None
    with open("indice.txt", "r", encoding="utf-8") as file_indice:
        for riga in file_indice:
            riga = riga.strip()
            if riga:
                parti = riga.split(',')
                if len(parti) == 2:
                    mat = parti[0]
                    pos = int(parti[1])
                    if mat == matricola_da_cercare:
                        posizione = pos
                        break
    
    if posizione is not None:
        # Apro il file binario e vado alla posizione specificata
        with open("studenti.dat", "rb") as file_bin:
            file_bin.seek(posizione)
            studente = pickle.load(file_bin)
            print(studente)
    else:
        print("Studente non trovato.")


# Creo i file
crea_file_studenti()

# Chiedo all'utente la matricola da cercare
matricola_input = input("Inserisci la matricola dello studente da cercare: ").upper()
cerca_studente_per_matricola(matricola_input)