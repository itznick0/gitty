import tkinter as tk
from tkinter import messagebox

class Salvadanaio:
    def __init__(self, root, dimensione="300x200"):
        self.totale = 0
        self.root = root
        self.finestra = tk.Toplevel(root)
        self.finestra.title("Salvadanaio")
        self.finestra.geometry(dimensione)
        self.finestra.configure(bg="#f0f0f0")
        label_titolo = tk.Label(self.finestra, text="Salvadanaio", bg="#4a7abc", fg="white", font=("Arial", 12, "bold"))
        label_titolo.pack()
        self.label_saldo = tk.Label(self.finestra, text=f"Saldo: {self.totale}€", bg="#f0f0f0", font=("Arial", 10))
        self.label_saldo.pack(pady=10)
        self.entry = tk.Entry(self.finestra, font=("Arial", 10))
        self.entry.pack(pady=5)
        btn_metti = tk.Button(self.finestra, text="Metti soldi", command=self.metti_soldi, bg="#4CAF50", fg="white", font=("Arial", 10))
        btn_metti.pack(pady=3)
        btn_visualizza = tk.Button(self.finestra, text="Visualizza saldo", command=self.visualizza_saldo, bg="#2196F3", fg="white", font=("Arial", 10))
        btn_visualizza.pack(pady=3)
        btn_svuota = tk.Button(self.finestra, text="Svuota salvadanaio", command=self.svuota_salvadanaio, bg="#f44336", fg="white", font=("Arial", 10))
        btn_svuota.pack(pady=3)
    def aggiungi(self, somma):
        if somma > 0:
            self.totale += somma
        else:
            messagebox.showerror("Errore", "La somma deve essere positiva.")
    def mostra_saldo(self):
        return self.totale
    def svuota(self):
        self.totale = 0
    def metti_soldi(self):
        try:
            somma = int(self.entry.get())
            self.aggiungi(somma)
        except ValueError:
            messagebox.showerror("Errore", "Inserisci un numero valido.")
        self.label_saldo.config(text=f"Saldo: {self.totale}€")
        self.entry.delete(0, tk.END)
    def visualizza_saldo(self):
        self.label_saldo.config(text=f"Saldo: {self.totale}€")
    def svuota_salvadanaio(self):
        self.svuota()
        self.label_saldo.config(text=f"Saldo: {self.totale}€")
class Fratello:
    def __init__(self, nome, cognome, root, dimensione="300x200"):
        self.nome = nome
        self.cognome = cognome
        self.salvadanaio_personale = Salvadanaio(root, dimensione)
    def metti_soldi_personale(self, somma):
        self.salvadanaio_personale.aggiungi(somma)
root = tk.Tk()
root.geometry("1x1+-1000+-1000")
salvadanaio_condiviso = Salvadanaio(root, "300x200+100+100")
mario = Fratello("Mario", "Rossi", root, "300x200+500+100")
luigi = Fratello("Luigi", "Rossi", root, "300x200+100+400")
root.mainloop()