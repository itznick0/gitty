filename="10_09.txt"

try:  
    with open(filename, "a") as pf:  
        for i in range(5):  
            nome = input(f"Inserisci il nome {i + 1} di 5: ")
            if nome:  
                pf.write(nome)
                pf.write("\n")
                print(f"'{nome}' è stato salvato correttamente nel file.")
            else:
                print("Non hai inserito nessun nome, passo al successivo.")
        print("Tutti i nomi inseriti sono stati aggiunti. File salvato correttamente.")
except IOError as e:
    print(f"Errore di I/O: Impossibile scrivere sul file '{filename}'.")
    print(f"Dettagli: {e}")
except Exception as e:
    print(f"Si è verificato un errore inaspettato: {e}")


try:
    with open(filename, "r") as pf:
        for riga in pf:
            print(riga.strip("\n"))
except FileNotFoundError:
    print(f"Errore: Il file '{filename}' non è stato trovato")
    print("Potresti dover prima eseguire uno script per scriverlo")

except IOError as e:
    print(f"Errore di I/O: Impossibile leggere il file '{filename}'")
    print(f"Dettagli: {e}")

except FileNotFoundError:
    print(f"Si è verificato un'errore insaspettato: {e}")

