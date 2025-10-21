import tkinter as tk
from tkinter import messagebox

class Salvadanaio:
    def __init__(self):
        self.totale = 0

    def aggiungi(self, somma):
        if somma > 0:
            self.totale += somma
            return True
        else:
            return False

    def mostra_saldo(self):
        return self.totale

    def svuota(self):
        self.totale = 0

class Fratello:
    def __init__(self, nome, cognome, salvadanaio):
        self.nome = nome
        self.cognome = cognome
        self.salvadanaio = salvadanaio

    def metti_soldi(self, somma):
        return self.salvadanaio.aggiungi(somma)

    def controlla_risparmi(self):
        return self.salvadanaio.mostra_saldo()

salvadanaio_famiglia = Salvadanaio()
mario = Fratello("Mario", "Rossi", salvadanaio_famiglia)
luigi = Fratello("Luigi", "Rossi", salvadanaio_famiglia)
fratello_corrente = mario

def seleziona_mario():
    global fratello_corrente
    fratello_corrente = mario
    label_fratello.config(text="Fratello attivo: Mario Rossi", fg="#2e7d32")

def seleziona_luigi():
    global fratello_corrente
    fratello_corrente = luigi
    label_fratello.config(text="Fratello attivo: Luigi Rossi", fg="#6a1b9a")

def aggiungi_soldi():
    try:
        somma = float(entry_somma.get())
    except ValueError:
        messagebox.showerror("Errore di Input", "Per favore, inserisci solo numeri validi.")
        return

    if fratello_corrente.metti_soldi(somma):
        entry_somma.delete(0, tk.END)
        aggiorna_saldo()
        label_messaggi.config(text=f"{fratello_corrente.nome} ha aggiunto {somma}€.", fg="#2e7d32")
    else:
        messagebox.showerror("Errore", "La somma deve essere positiva.")

def controlla_saldo():
    saldo = fratello_corrente.controlla_risparmi()
    label_saldo.config(text=f"Saldo attuale: {saldo}€")
    label_messaggi.config(text="Saldo visualizzato.", fg="#1565c0")

def svuota_salvadanaio():
    salvadanaio_famiglia.svuota()
    aggiorna_saldo()
    label_messaggi.config(text="Il salvadanaio è stato svuotato.", fg="#e65100")

def aggiorna_saldo():
    saldo = salvadanaio_famiglia.mostra_saldo()
    label_saldo.config(text=f"Saldo attuale: {saldo}€")

root = tk.Tk()
root.title("Salvadanaio di Famiglia")
root.geometry("420x480")
root.configure(bg="#f0f8ff")

tk.Label(root, text="💰 Salvadanaio Condiviso", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#1a237e").pack(pady=12)

tk.Label(root, text="Scegli il fratello:", font=("Helvetica", 11), bg="#f0f8ff", fg="#37474f").pack(pady=4)
tk.Button(root, text="Mario Rossi", command=seleziona_mario, bg="#c8e6c9", fg="#2e7d32", font=("Helvetica", 10, "bold"), width=20).pack(pady=3)
tk.Button(root, text="Luigi Rossi", command=seleziona_luigi, bg="#e1bee7", fg="#6a1b9a", font=("Helvetica", 10, "bold"), width=20).pack(pady=3)

label_fratello = tk.Label(root, text="Fratello attivo: Mario Rossi", font=("Helvetica", 10, "bold"), bg="#f0f8ff", fg="#2e7d32")
label_fratello.pack(pady=6)

tk.Label(root, text="Somma da aggiungere (€):", font=("Helvetica", 11), bg="#f0f8ff", fg="#37474f").pack(pady=4)
entry_somma = tk.Entry(root, font=("Helvetica", 12), justify="center", width=15)
entry_somma.pack(pady=6)

tk.Button(root, text="Aggiungi soldi", command=aggiungi_soldi, bg="#4caf50", fg="white", font=("Helvetica", 11, "bold"), width=20).pack(pady=5)
tk.Button(root, text="Controlla saldo", command=controlla_saldo, bg="#2196f3", fg="white", font=("Helvetica", 11, "bold"), width=20).pack(pady=5)
tk.Button(root, text="Svuota salvadanaio", command=svuota_salvadanaio, bg="#f44336", fg="white", font=("Helvetica", 11, "bold"), width=20).pack(pady=8)

label_saldo = tk.Label(root, text="Saldo attuale: 0€", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#0d47a1")
label_saldo.pack(pady=10)

label_messaggi = tk.Label(root, text="", font=("Helvetica", 10), bg="#f0f8ff", fg="#5d4037")
label_messaggi.pack(pady=6)

root.mainloop()