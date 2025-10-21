import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

SCORTA_FILE = "scorta_merende.txt"
COMBINAZIONI_FILE = "combinazioni_merende.txt"

def carica_scorta():
    if os.path.exists(SCORTA_FILE):
        with open(SCORTA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {"merende": [], "bevande": []}

def salva_scorta(scorta):
    with open(SCORTA_FILE, "w", encoding="utf-8") as f:
        json.dump(scorta, f, indent=4, ensure_ascii=False)

def aggiungi_merenda():
    nome = input("Nome merenda: ").strip()
    if not nome:
        print("❌ Nome non valido.")
        return
    try:
        quantita = int(input("Quantità disponibile: "))
        peso = int(input("Peso (1 = serve un'altra cosa, 2 = basta da sola): "))
        if peso not in [1, 2]:
            print("❌ Peso deve essere 1 o 2.")
            return
    except ValueError:
        print("❌ Inserisci numeri validi.")
        return

    scorta = carica_scorta()
    scorta["merende"].append({"nome": nome, "quantita": quantita, "peso": peso})
    salva_scorta(scorta)
    print(f"✅ Aggiunta merenda: {nome} (x{quantita}, peso={peso})")

def aggiungi_bevanda():
    nome = input("Nome bevanda: ").strip()
    if not nome:
        print("❌ Nome non valido.")
        return
    try:
        quantita = int(input("Quantità disponibile: "))
    except ValueError:
        print("❌ Inserisci un numero valido.")
        return

    scorta = carica_scorta()
    scorta["bevande"].append({"nome": nome, "quantita": quantita})
    salva_scorta(scorta)
    print(f"✅ Aggiunta bevanda: {nome} (x{quantita})")

def registra_consumo():
    scorta = carica_scorta()
    tipo = input("Cosa hai consumato? (m = merenda, b = bevanda): ").strip().lower()
    
    if tipo == "m":
        lista = scorta["merende"]
        tipo_nome = "merenda"
    elif tipo == "b":
        lista = scorta["bevande"]
        tipo_nome = "bevanda"
    else:
        print("❌ Scelta non valida.")
        return

    if not lista:
        print(f"❌ Nessuna {tipo_nome} disponibile.")
        return

    print(f"\n📦 {tipo_nome.capitalize()} disponibili:")
    for i, item in enumerate(lista):
        print(f"{i+1}. {item['nome']} (rimasti: {item['quantita']})")

    try:
        scelta = int(input(f"Quale {tipo_nome} hai consumato? (numero): ")) - 1
        if scelta < 0 or scelta >= len(lista):
            raise ValueError
    except ValueError:
        print("❌ Scelta non valida.")
        return

    if lista[scelta]["quantita"] <= 0:
        print("❌ Quantità esaurita!")
        return

    lista[scelta]["quantita"] -= 1
    print(f"✅ Registrato consumo di: {lista[scelta]['nome']}")

    # Rimuovi se quantità zero
    if lista[scelta]["quantita"] == 0:
        del lista[scelta]
        print("🗑️ Oggetto rimosso (quantità zero).")

    salva_scorta(scorta)

def genera_combinazioni():
    scorta = carica_scorta()
    merende = scorta["merende"]
    bevande = scorta["bevande"]

    if not merende or not bevande:
        print("❌ Devi avere almeno una merenda e una bevanda per generare combinazioni.")
        return

    combinazioni = []

    # Separiamo merende leggere (peso=1) da quelle consistenti (peso=2)
    leggere = [m for m in merende if m["peso"] == 1]
    consistenti = [m for m in merende if m["peso"] == 2]

    # Combinazioni con merende consistenti (basta una)
    for m in consistenti:
        for b in bevande:
            combinazioni.append(f"MERENDA: {m['nome']} (consistente) + BEVANDA: {b['nome']}")

    # Combinazioni con DUE merende leggere (per fare una merenda completa)
    for i, m1 in enumerate(leggere):
        for m2 in leggere[i:]:  # da i in poi per evitare doppioni (es. biscottoA + biscottoB e viceversa)
            if m1 == m2 and m1["quantita"] < 2:
                continue  # non posso usare due volte lo stesso se ne ho solo uno
            for b in bevande:
                if m1 == m2:
                    combinazioni.append(f"MERENDA: 2x {m1['nome']} + BEVANDA: {b['nome']}")
                else:
                    combinazioni.append(f"MERENDA: {m1['nome']} + {m2['nome']} + BEVANDA: {b['nome']}")

    # Salva su file
    with open(COMBINAZIONI_FILE, "w", encoding="utf-8") as f:
        f.write("📋 TUTTE LE COMBINAZIONI POSSIBILI MERENDA + BEVANDA\n")
        f.write("="*60 + "\n\n")
        for i, comb in enumerate(combinazioni, 1):
            f.write(f"{i}. {comb}\n")

    print(f"✅ Generata lista di {len(combinazioni)} combinazioni in '{COMBINAZIONI_FILE}'")

def mostra_scorta():
    scorta = carica_scorta()
    print("\n📦 SCORTA ATTUALE")
    print("="*40)

    print("\n🍪 MERENDE:")
    for m in scorta["merende"]:
        tipo = "leggera (servono 2)" if m["peso"] == 1 else "consistente (basta 1)"
        print(f" - {m['nome']} (x{m['quantita']}) → {tipo}")

    print("\n🥤 BEVANDE:")
    for b in scorta["bevande"]:
        print(f" - {b['nome']} (x{b['quantita']})")

    if not scorta["merende"] and not scorta["bevande"]:
        print(" ❌ Nessun elemento in scorta.")

def menu():
    while True:
        print("\n" + "="*50)
        print("   🍎 GESTORE MERENDE SCUOLA 🍌")
        print("="*50)
        print("1. ➕ Aggiungi merenda")
        print("2. ➕ Aggiungi bevanda")
        print("3. 🗑️  Registra consumo (merenda o bevanda)")
        print("4. 🔄 Genera tutte le combinazioni merenda+bevanda")
        print("5. 📦 Mostra scorta attuale")
        print("0. ❌ Esci")
        print("="*50)

        scelta = input("Scegli un'opzione: ").strip()

        if scelta == "1":
            aggiungi_merenda()
        elif scelta == "2":
            aggiungi_bevanda()
        elif scelta == "3":
            registra_consumo()
        elif scelta == "4":
            genera_combinazioni()
        elif scelta == "5":
            mostra_scorta()
        elif scelta == "0":
            print("👋 Arrivederci!")
            break
        else:
            print("❌ Opzione non valida.")

if __name__ == "__main__":
    menu()