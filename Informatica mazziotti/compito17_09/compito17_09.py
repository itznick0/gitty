import os

# assicurarsi che il programma lavori nella cartella dello script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename1 = "compito17_09.txt"
filename2 = "compito17_09-2.txt"

classe_scelta = input("Inserisci la classe (1P, 2P, 3P, 4P): ").strip()

try:
    with open(filename1, "r") as pf:
        with open(filename2, "w") as pf1:
            posizione = None
            studenti = []
            trovata = False

            while True:
                riga = pf.readline()
                if not riga:
                    break

                riga = riga.strip()

                if not trovata:
                    if riga == classe_scelta:
                        posizione = pf.tell()
                        trovata = True
                else:
                    if riga in ("1P", "2P", "3P", "4P"):
                        break
                    studenti.append(riga)

            if trovata:
                pf1.write(classe_scelta + " (Posizione " + str(posizione) + ")\n")
                for studente in studenti:
                    pf1.write(studente + "\n")
                print("Classe " + classe_scelta + " salvata correttamente nel file con posizione " + str(posizione) + ".")
            else:
                print("Classe " + classe_scelta + " non trovata nel file.")

except IOError as e:
    print("Errore di I/O: Impossibile accedere al file '" + filename1 + "'.")
    print("Dettagli: " + str(e))
except Exception as e:
    print("Si è verificato un errore inaspettato: " + str(e))
