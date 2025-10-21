import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filename1 = "10_09.txt"
filename2 = "10_09-2.txt"

try:
    with open(filename1, "r+") as pf, open(filename2, "w") as pf1:
        posizione = pf.tell()
        nome = pf.readline()
        while nome:
            pf1.write("posizione= "+str(posizione))
            pf1.write("\n")
            posizione = pf.tell()
            nome = pf.readline()
            print(f"La posizione n°:{posizione} è stata salvata correttamente nel file.")
        pf.seek(65)
        nome=pf.readline()
        print(nome)
except IOError as e:
    print(f"Errore di I/O: Impossibile scrivere sul file '{filename1}'.")
    print(f"Dettagli: {e}")
except Exception as e:
    print(f"Si è verificato un errore inaspettato: {e}")
