import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog, Listbox, Toplevel, ttk

SCORTA_FILE = "scorta_merende.txt"
COMBINAZIONI_FILE = "combinazioni_merende.txt"

# --- Funzioni di backend (uguali al testuale) ---

def carica_scorta():
    if os.path.exists(SCORTA_FILE):
        with open(SCORTA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {"merende": [], "bevande": []}

def salva_scorta(scorta):
    with open(SCORTA_FILE, "w", encoding="utf-8") as f:
        json.dump(scorta, f, indent=4, ensure_ascii=False)

def aggiungi_merenda_gui(nome, quantita, peso, window):
    if not nome.strip():
        messagebox.showerror("Errore", "Il nome non può essere vuoto!")
        return
    try:
        quantita = int(quantita)
        peso = int(peso)
        if peso not in [1, 2]:
            raise ValueError
    except ValueError:
        messagebox.showerror("Errore", "Quantità deve essere un numero, peso 1 o 2.")
        return

    scorta = carica_scorta()
    scorta["merende"].append({"nome": nome, "quantita": quantita, "peso": peso})
    salva_scorta(scorta)
    messagebox.showinfo("Successo", f"Merenda '{nome}' aggiunta!")
    window.destroy()
    aggiorna_liste()

def aggiungi_bevanda_gui(nome, quantita, window):
    if not nome.strip():
        messagebox.showerror("Errore", "Il nome non può essere vuoto!")
        return
    try:
        quantita = int(quantita)
    except ValueError:
        messagebox.showerror("Errore", "Quantità deve essere un numero.")
        return

    scorta = carica_scorta()
    scorta["bevande"].append({"nome": nome, "quantita": quantita})
    salva_scorta(scorta)
    messagebox.showinfo("Successo", f"Bevanda '{nome}' aggiunta!")
    window.destroy()
    aggiorna_liste()

def registra_consumo_gui(tipo, indice):
    scorta = carica_scorta()
    if tipo == "merenda":
        lista = scorta["merende"]
    else:
        lista = scorta["bevande"]

    if indice < 0 or indice >= len(lista):
        messagebox.showerror("Errore", "Selezione non valida.")
        return

    if lista[indice]["quantita"] <= 0:
        messagebox.showwarning("Attenzione", "Quantità esaurita!")
        return

    lista[indice]["quantita"] -= 1
    nome = lista[indice]["nome"]
    messagebox.showinfo("Consumato", f"Hai consumato: {nome}")

    if lista[indice]["quantita"] == 0:
        del lista[indice]
        messagebox.showinfo("Rimosso", f"{nome} rimosso (quantità zero).")

    salva_scorta(scorta)
    aggiorna_liste()

def genera_combinazioni_gui():
    scorta = carica_scorta()
    merende = scorta["merende"]
    bevande = scorta["bevande"]

    if not merende or not bevande:
        messagebox.showwarning("Attenzione", "Aggiungi almeno una merenda e una bevanda!")
        return

    combinazioni = []
    leggere = [m for m in merende if m["peso"] == 1]
    consistenti = [m for m in merende if m["peso"] == 2]

    for m in consistenti:
        for b in bevande:
            combinazioni.append(f"MERENDA: {m['nome']} (consistente) + BEVANDA: {b['nome']}")

    for i, m1 in enumerate(leggere):
        for m2 in leggere[i:]:
            if m1 == m2 and m1["quantita"] < 2:
                continue
            for b in bevande:
                if m1 == m2:
                    combinazioni.append(f"MERENDA: 2x {m1['nome']} + BEVANDA: {b['nome']}")
                else:
                    combinazioni.append(f"MERENDA: {m1['nome']} + {m2['nome']} + BEVANDA: {b['nome']}")

    with open(COMBINAZIONI_FILE, "w", encoding="utf-8") as f:
        f.write("📋 TUTTE LE COMBINAZIONI POSSIBILI MERENDA + BEVANDA\n")
        f.write("="*60 + "\n\n")
        for i, comb in enumerate(combinazioni, 1):
            f.write(f"{i}. {comb}\n")

    messagebox.showinfo("Combinazioni", f"Generata lista di {len(combinazioni)} combinazioni in '{COMBINAZIONI_FILE}'")

# --- Funzioni GUI ---

def apri_finestra_aggiungi_merenda():
    win = Toplevel(root)
    win.title("➕ Aggiungi Merenda")
    win.geometry("350x200")
    win.resizable(False, False)

    tk.Label(win, text="Nome merenda:").pack(pady=5)
    entry_nome = tk.Entry(win, width=40)
    entry_nome.pack(pady=5)

    tk.Label(win, text="Quantità:").pack(pady=5)
    entry_quantita = tk.Entry(win, width=10)
    entry_quantita.pack(pady=5)

    tk.Label(win, text="Peso (1=leggera, 2=consistente):").pack(pady=5)
    entry_peso = tk.Entry(win, width=10)
    entry_peso.pack(pady=5)

    btn = tk.Button(win, text="✅ Aggiungi",
                    command=lambda: aggiungi_merenda_gui(
                        entry_nome.get(),
                        entry_quantita.get(),
                        entry_peso.get(),
                        win))
    btn.pack(pady=10)

def apri_finestra_aggiungi_bevanda():
    win = Toplevel(root)
    win.title("➕ Aggiungi Bevanda")
    win.geometry("350x150")
    win.resizable(False, False)

    tk.Label(win, text="Nome bevanda:").pack(pady=5)
    entry_nome = tk.Entry(win, width=40)
    entry_nome.pack(pady=5)

    tk.Label(win, text="Quantità:").pack(pady=5)
    entry_quantita = tk.Entry(win, width=10)
    entry_quantita.pack(pady=5)

    btn = tk.Button(win, text="✅ Aggiungi",
                    command=lambda: aggiungi_bevanda_gui(
                        entry_nome.get(),
                        entry_quantita.get(),
                        win))
    btn.pack(pady=10)

def apri_finestra_consuma(tipo):
    scorta = carica_scorta()
    if tipo == "merenda":
        lista = scorta["merende"]
        titolo = "🗑️ Consuma Merenda"
    else:
        lista = scorta["bevande"]
        titolo = "🗑️ Consuma Bevanda"

    if not lista:
        messagebox.showwarning("Attenzione", f"Nessuna {tipo} disponibile!")
        return

    win = Toplevel(root)
    win.title(titolo)
    win.geometry("400x300")

    tk.Label(win, text=f"Seleziona {tipo} da consumare:", font=("Arial", 10, "bold")).pack(pady=10)

    listbox = Listbox(win, width=60, height=10)
    listbox.pack(pady=10)

    for item in lista:
        if tipo == "merenda":
            peso_str = " (leggera)" if item["peso"] == 1 else " (consistente)"
            listbox.insert(tk.END, f"{item['nome']} - rimasti: {item['quantita']}{peso_str}")
        else:
            listbox.insert(tk.END, f"{item['nome']} - rimasti: {item['quantita']}")

    def conferma_consumo():
        selezione = listbox.curselection()
        if not selezione:
            messagebox.showwarning("Attenzione", "Seleziona un elemento!")
            return
        registra_consumo_gui(tipo, selezione[0])
        win.destroy()

    tk.Button(win, text="✅ Consuma", command=conferma_consumo, bg="#4CAF50", fg="white").pack(pady=10)

def aggiorna_liste():
    # Pulisci liste
    listbox_merende.delete(0, tk.END)
    listbox_bevande.delete(0, tk.END)

    scorta = carica_scorta()

    for m in scorta["merende"]:
        peso_str = " 🍪 (leggera)" if m["peso"] == 1 else " 🍫 (consistente)"
        listbox_merende.insert(tk.END, f"{m['nome']} x{m['quantita']}{peso_str}")

    for b in scorta["bevande"]:
        listbox_bevande.insert(tk.END, f"{b['nome']} x{b['quantita']} 🥤")

# --- Interfaccia Principale ---

root = tk.Tk()
root.title("🍎 GESTORE MERENDE SCUOLA 🍌")
root.geometry("700x600")
root.resizable(False, False)

# Titolo
tk.Label(root, text="🍎 GESTORE MERENDE SCUOLA 🍌", font=("Arial", 16, "bold")).pack(pady=10)

# Frame pulsanti
frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="➕ Aggiungi Merenda", command=apri_finestra_aggiungi_merenda,
          width=20, bg="#2196F3", fg="white").grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_btn, text="➕ Aggiungi Bevanda", command=apri_finestra_aggiungi_bevanda,
          width=20, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_btn, text="🗑️ Consuma Merenda", command=lambda: apri_finestra_consuma("merenda"),
          width=20, bg="#FF5722", fg="white").grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_btn, text="🗑️ Consuma Bevanda", command=lambda: apri_finestra_consuma("bevanda"),
          width=20, bg="#FF5722", fg="white").grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame_btn, text="🔄 Genera Combinazioni", command=genera_combinazioni_gui,
          width=44, bg="#4CAF50", fg="white").grid(row=2, column=0, columnspan=2, pady=10)

# Frame scorta
frame_scorta = tk.Frame(root)
frame_scorta.pack(pady=10, fill="both", expand=True)

tk.Label(frame_scorta, text="🍪 MERENDE:", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", padx=10)
tk.Label(frame_scorta, text="🥤 BEVANDE:", font=("Arial", 12, "bold")).grid(row=0, column=1, sticky="w", padx=10)

listbox_merende = Listbox(frame_scorta, width=40, height=15, font=("Courier", 10))
listbox_merende.grid(row=1, column=0, padx=10, pady=5)

listbox_bevande = Listbox(frame_scorta, width=40, height=15, font=("Courier", 10))
listbox_bevande.grid(row=1, column=1, padx=10, pady=5)

# Bottone refresh (opzionale, utile se modifichi file manualmente)
tk.Button(root, text="↻ Aggiorna Lista", command=aggiorna_liste,
          bg="#9E9E9E", fg="white").pack(pady=5)

# Carica inizialmente i dati
aggiorna_liste()

# Avvia GUI
root.mainloop()