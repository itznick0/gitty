import os
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from collections import Counter

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Configurazione Iniziale
BASE_URL = 'http://quotes.toscrape.com'
ALL_QUOTES = []
FIELDNAMES = ['autore', 'citazione']

# Configurazione dei percorsi con il modulo os
OUTPUT_DIR = 'analisi_citazioni_output'
CSV_FILENAME = os.path.join(OUTPUT_DIR, 'citazioni_scraper.csv')
ANALYSIS_FILENAME = os.path.join(OUTPUT_DIR, 'analisi_top.txt') 

# Creazione della cartella di output
try:
    os.makedirs(OUTPUT_DIR, exist_ok=True) 
except Exception:
    pass

# Web Scraping Basato sul Paginatore
current_url = BASE_URL 
page_count = 0

while current_url:
    url = current_url
    page_count += 1
    current_url = None 

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')

        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            ALL_QUOTES.append({'autore': author, 'citazione': text})
            
        next_li = soup.find('li', class_='next') 

        if next_li:
            next_a = next_li.find('a')
            if next_a and 'href' in next_a.attrs:
                current_url = BASE_URL + next_a['href']
                
    except requests.exceptions.RequestException:
        break
    except AttributeError:
        break

# Salvataggio su CSV
with open(CSV_FILENAME, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
    writer.writeheader()
    writer.writerows(ALL_QUOTES)

# Analisi Dati con Pandas
df = pd.read_csv(CSV_FILENAME)

# Analisi Base
autori_top_5 = df['autore'].value_counts().head(5)

all_text = ' '.join(df['citazione'].fillna(''))
words = all_text.lower().split()
word_counts = Counter(words)
parole_top_10 = word_counts.most_common(10)

# Analisi Avanzata (Lunghezza Citazioni)
df['lunghezza_citazione'] = df['citazione'].apply(lambda x: len(str(x)))
lunghezza_media_autore = df.groupby('autore')['lunghezza_citazione'].mean()
top_autori_lunghezza = lunghezza_media_autore.sort_values(ascending=False).head(5)

# Salvataggio dell'Analisi
with open(ANALYSIS_FILENAME, 'w', encoding='utf-8') as f:
    f.write("--- Risultati Analisi Web Scraping ---\n\n")
    
    f.write("Autori più citati (Top 5):\n")
    f.write(autori_top_5.to_string())
    f.write("\n\n" + "-"*40 + "\n\n")

    f.write("Parole più comuni (Top 10):\n")
    f.write(str(parole_top_10)) 
    f.write("\n\n" + "-"*40 + "\n\n")
    
    f.write("Autori con Citazioni Più Lunghe (Media Lunghezza Caratteri):\n")
    f.write(top_autori_lunghezza.to_string())