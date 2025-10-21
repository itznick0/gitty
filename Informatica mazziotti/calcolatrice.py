import tkinter as tk
import datatime from datetime


# Funzione per gestire il click di un numero o di un operatore
def on_button_click(char):
    """Aggiunge il carattere premuto al display."""
    display.insert(tk.END, char)

# Funzione per gestire il click del pulsante "="
def calculate():
    """Esegue il calcolo dell'espressione nel display."""
    try:
        # Prende l'intera espressione dal display
        expression = display.get()
        # Usa eval() per calcolare il risultato in modo sicuro in questo contesto
        # Nota: eval() può essere un rischio per la sicurezza se l'input non è controllato.
        # Qui è sicuro perché l'input proviene solo dai nostri pulsanti.
        result = eval(expression)
       
        # Pulisce il display e mostra il risultato
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        # In caso di errore (es. "5*/" o divisione per zero), mostra "Errore"
        display.delete(0, tk.END)
        display.insert(0, "Errore")
        print(f"Errore: {e}")

# Funzione per pulire il display
def clear_display():
    """Pulisce il campo di input."""
    display.delete(0, tk.END)

# --- Creazione della Finestra Principale ---
root = tk.Tk()
root.title("Calcolatrice")
root.geometry("300x400")
root.resizable(False, False) # Impedisce di ridimensionare la finestra
root.configure(bg="#f0f0f0") # Un colore di sfondo più neutro

# --- Creazione del Display ---
# 1. Creazione
display = tk.Entry(root)
# 2. Configurazione
display.config(font=("Arial", 24),
               borderwidth=2,
               relief="sunken",
               justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
button_layout = [
    ['7', '8', '9', 'Transizione'],
    ['4', '5', '6', 'Mostra saldo'],
    ['1', '2', '3', 'Preleva'],
    ['C', '0', 'Esc', 'Deposita']
]

for i, row in enumerate(button_layout):
    for j, char in enumerate(row):
        if char == 'C':
            commandx= clear_display
        elif char == 'Esc':
            commandx = calculate
        elif char == 'Transizione':
            commandx = lambda: on_button_click('/')
        elif char == 'Mostra saldo':
            commandx = lambda: on_button_click('*')
        elif char == 'Preleva':
            commandx = lambda: on_button_click('-')
        elif char == 'Deposita':
            commandx = lambda: on_button_click('+')
        else:
            commandx = lambda c=char: on_button_click(c)
       
        button = tk.Button(root)
        button.config(text=char,
                      font=("Arial", 14),
                      width=5,
                      height=2,
                      command=commandx)
        button.grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")

# Configura le colonne e le righe per espandersi uniformemente
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()