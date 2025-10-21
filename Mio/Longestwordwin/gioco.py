import os
import random
import threading
import time
from datetime import datetime

CATEGORIES_DIR = "categorie"
HISTORY_FILE = "games_history.txt"
RECORDS_FILE = "records.txt"

# Schema di aumento della lava: [round 1, round 2, ...]
LAVA_INCREASE = [0, 1, 2, 4, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 10, 10, 10, 10, 10, 12]
# Dopo il round 20, la lava sale sempre di 12 metri per round
LAVA_INCREASE += [12] * 100  # esteso a 120 round

def load_categories():
    if not os.path.exists(CATEGORIES_DIR):
        print(f"❌ Cartella '{CATEGORIES_DIR}' non trovata!")
        exit(1)
    categories = {}
    for file in os.listdir(CATEGORIES_DIR):
        if file.endswith(".txt"):
            name = file.replace(".txt", "")
            path = os.path.join(CATEGORIES_DIR, file)
            with open(path, "r", encoding="utf-8") as f:
                words = set(line.strip() for line in f if line.strip())
            if words:
                categories[name] = words
    return categories

def get_player_names():
    while True:
        try:
            num = int(input("Quanti giocatori? (1-4): "))
            if 1 <= num <= 4:
                break
            else:
                print("Inserisci un numero tra 1 e 4.")
        except ValueError:
            print("Inserisci un numero valido.")
    
    players = []
    for i in range(num):
        name = input(f"Nome giocatore {i+1}: ").strip()
        if not name:
            name = f"Giocatore{i+1}"
        players.append(name)
    return players

def save_game_result(players, scores, round_reached):
    """Salva la partita in games_history.txt"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n--- Partita del {timestamp} ---\n")
        for p, s in zip(players, scores):
            f.write(f"{p}: {s} metri (sopravvissuto {round_reached} round)\n")
        f.write("-" * 40 + "\n")

def load_records():
    """Carica i record: {'globale': (nome, punteggio), 'Giocatore1': punteggio, ...}"""
    records = {"globale": ("", 0)}
    if os.path.exists(RECORDS_FILE):
        with open(RECORDS_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("Globale:"):
                    parts = line.replace("Globale:", "").strip().split(" - ")
                    if len(parts) == 2:
                        records["globale"] = (parts[0], int(parts[1]))
                elif ":" in line:
                    name, score = line.strip().split(": ")
                    records[name] = int(score)
    return records

def save_records(records):
    """Salva i record su file"""
    with open(RECORDS_FILE, "w", encoding="utf-8") as f:
        # Record globale
        name, score = records["globale"]
        f.write(f"Globale: {name} - {score}\n")
        f.write("\nRecord per giocatore:\n")
        for name, score in records.items():
            if name != "globale":
                f.write(f"{name}: {score}\n")

def play_round(category_name, word_set, player_name, round_num):
    """Gioca un round per un giocatore. Restituisce (distanza aggiunta, parola valida?)"""
    print(f"\n{'='*50}")
    print(f"ROUND {round_num} - Tocca a: {player_name}")
    print(f"🔥 Categoria: {category_name}")
    print("="*50)

    user_input = [None]
    timer_expired = [False]

    def get_input():
        user_input[0] = input("Scrivi una parola ➡️  ").strip().lower()

    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()
    input_thread.join(timeout=20)

    if input_thread.is_alive():
        timer_expired[0] = True
        print("\n⏰ TEMPO SCADUTO!")

    word = user_input[0] if not timer_expired[0] else None

    if word and word in word_set:
        distance = len(word)
        print(f"✅ Parola valida! +{distance} metri")
        return distance, True
    elif word:
        print("❌ Parola non valida per questa categoria!")
        return 0, False
    else:
        print("⏭️ Nessuna parola inserita.")
        return 0, False

def main():
    print("🌋 LAVA ESCAPE - Modalità Multiplayer!")
    print("Sopravvivi all'eruzione con i tuoi amici!")
    input("\nPremi INVIO per iniziare...")

    categories = load_categories()
    players = get_player_names()
    num_players = len(players)
    
    # Inizializza punteggi
    total_distances = [0] * num_players
    active_players = list(range(num_players))  # indici dei giocatori ancora in gioco
    round_num = 1

    # Carica record esistenti
    records = load_records()

    while active_players and round_num <= len(LAVA_INCREASE):
        # Calcola altezza lava DOPO questo round
        lava_increase = LAVA_INCREASE[round_num - 1]  # round 1 → indice 0
        lava_height = sum(LAVA_INCREASE[:round_num])  # somma cumulativa

        # Turno di ogni giocatore attivo
        next_active = []
        for idx in active_players:
            category_name = random.choice(list(categories.keys()))
            word_set = categories[category_name]
            dist, valid = play_round(category_name, word_set, players[idx], round_num)
            total_distances[idx] += dist

            # Controlla se è ancora vivo
            if total_distances[idx] > lava_height:
                print(f"✅ {players[idx]} è al sicuro! ({total_distances[idx]}m > {lava_height}m)")
                next_active.append(idx)
            else:
                print(f"💀 {players[idx]} è stato raggiunto dalla lava! ({total_distances[idx]}m ≤ {lava_height}m)")

        active_players = next_active
        round_num += 1

        if active_players:
            print(f"\n🏁 Fine round {round_num - 1}. Prossimo round...")
            time.sleep(2)

    # Fine del gioco
    print("\n" + "="*50)
    print("📊 RISULTATI FINALI")
    print("="*50)
    for i, name in enumerate(players):
        print(f"{name}: {total_distances[i]} metri")
    
    max_score = max(total_distances)
    winners = [players[i] for i, s in enumerate(total_distances) if s == max_score]
    print(f"\n🏆 Vincitore/i: {', '.join(winners)} con {max_score} metri!")

    # Aggiorna record
    for i, name in enumerate(players):
        score = total_distances[i]
        # Record personale
        if name not in records or score > records[name]:
            records[name] = score
        # Record globale
        if score > records["globale"][1]:
            records["globale"] = (name, score)

    save_records(records)
    save_game_result(players, total_distances, round_num - 1)

    print(f"\n📈 Record globale: {records['globale'][0]} - {records['globale'][1]} metri")
    print(f"📁 Partita salvata in '{HISTORY_FILE}'")

if __name__ == "__main__":
    main()