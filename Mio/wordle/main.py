import os
import random
import requests
from deep_translator import GoogleTranslator

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def download_and_filter_words(output_file):
    print("Scaricando le parole...")
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    try:
        response = requests.get(url)
        words = [w.strip().lower() for w in response.text.splitlines() if len(w.strip()) == 5]
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(words))
        print(f"✅ File '{output_file}' creato con {len(words)} parole di 5 lettere.")
    except Exception as e:
        print(f"❌ Errore nel download: {e}")

def load_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip().lower() for line in f if len(line.strip()) == 5]
    except FileNotFoundError:
        return []

def load_history(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return set(line.strip().lower().split(' - ')[0] for line in f)
    except FileNotFoundError:
        return set()

def save_history(word, filename, result):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"{word} - {result}\n")

def check_guess_detailed(guess, word):
    word_chars = list(word)
    guess_chars = list(guess)
    result = [''] * 5

    for i in range(5):
        if guess_chars[i] == word_chars[i]:
            result[i] = '✅'
            word_chars[i] = None
            guess_chars[i] = None

    for i in range(5):
        if guess_chars[i] is not None:
            if guess_chars[i] in word_chars:
                result[i] = '🟡'
                word_chars[word_chars.index(guess_chars[i])] = None
            else:
                result[i] = '❌'

    return result

def analyze_guess(guess, word):
    result = check_guess_detailed(guess, word)
    giuste_pos = []
    sbagliate_pos = []
    sbagliate_lettere = []

    for i, char in enumerate(guess):
        if result[i] == '✅':
            giuste_pos.append((char, i + 1))
        elif result[i] == '🟡':
            sbagliate_pos.append((char, i + 1))
        elif result[i] == '❌':
            sbagliate_lettere.append(char)

    return giuste_pos, sbagliate_pos, sbagliate_lettere

def get_translation(word):
    try:
        traduzione = GoogleTranslator(source='en', target='it').translate(word)
        return traduzione
    except Exception as e:
        return "traduzione non disponibile"

def main():
    parole_file = 'parole.txt'
    storia_file = 'storia.txt'

    if not load_words(parole_file):
        download_and_filter_words(parole_file)

    parole = load_words(parole_file)
    storia = load_history(storia_file)

    parole_disponibili = [p for p in parole if p not in storia]

    if not parole_disponibili:
        print("⚠️ Non ci sono più parole disponibili!")
        return

    parola_da_indovinare = random.choice(parole_disponibili)
    tentativi = 0
    max_tentativi = 6

    print("="*50)
    print("🎮 WORDLE INGLESE — Indovina la parola di 5 lettere!")
    print("Legenda:")
    print("✅ = Lettera giusta e in posizione giusta")
    print("🟡 = Lettera presente ma in posizione sbagliata")
    print("❌ = Lettera non presente nella parola")
    print("="*50)

    while tentativi < max_tentativi:
        tentativi += 1
        guess = input(f"\nTentativo {tentativi}/{max_tentativi}: ").strip().lower()

        if len(guess) != 5:
            print("❌ La parola deve essere di 5 lettere.")
            tentativi -= 1
            continue

        if guess not in parole:
            print("❌ Parola non valida (non presente nell'elenco).")
            tentativi -= 1
            continue

        giuste_pos, sbagliate_pos, sbagliate_lettere = analyze_guess(guess, parola_da_indovinare)
        risultato = check_guess_detailed(guess, parola_da_indovinare)

        print(f"{guess.upper()} → {' '.join(risultato)}")

        if giuste_pos:
            print("Lettere corrette in posizione giusta:", ', '.join([f"{c} ({p})" for c, p in giuste_pos]))
        if sbagliate_pos:
            print("Lettere corrette in posizione sbagliata:", ', '.join([f"{c} ({p})" for c, p in sbagliate_pos]))
        if sbagliate_lettere:
            print("Lettere sbagliate:", ', '.join(sbagliate_lettere))

        if guess == parola_da_indovinare:
            traduzione = get_translation(parola_da_indovinare)
            print(f"\n🎉 COMPLIMENTI! Hai indovinato la parola: {parola_da_indovinare.upper()} ({traduzione})")
            save_history(parola_da_indovinare, storia_file, "indovinata")
            return

    traduzione = get_translation(parola_da_indovinare)
    print(f"\n💔 Hai finito i tentativi. La parola era: {parola_da_indovinare.upper()} ({traduzione})")
    save_history(parola_da_indovinare, storia_file, "non indovinata")

if __name__ == "__main__":
    main()