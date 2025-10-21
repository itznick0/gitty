import os 
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from collections import Counter

os.chdir(os.path.dirname(os.path.abspath(__file__)))

BASE_URL = 'http://quotes.toscrape.com'
ALL_QUOTES = []
CSV_FILENAME = 'citazioni.csv'
FIELDNAMES = ['autore', 'citazione']
PAGE_RANGE = range(1, 11)

for page in PAGE_RANGE:
    url = f'{BASE_URL}/page/{page}/'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        ALL_QUOTES.append({'autore': author, 'citazione': text})
    
with open(CSV_FILENAME, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
    writer.writeheader()
    writer.writerows(ALL_QUOTES)

df = pd.read_csv(CSV_FILENAME)

print(" Prime 5 righe del dataset:")
print(df.head())

print("\n Autori più citati (Top 5):")
print(df['autore'].value_counts().head(5))

all_text = ' '.join(df['citazione'])
words = all_text.lower().split()
word_counts = Counter(words)

print("\n Parole più comuni (Top 10):")
print(word_counts.most_common(10))