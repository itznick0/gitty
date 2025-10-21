import requests
from bs4 import BeautifulSoup 

url = "https://www.iiscopernico.edu.it/eventi/1155-errori-negli-elenchi-dei-libri-di-testo"
    
print(f"--- Fase 1: Raccolta dati da {url} ---")
    
try:
        response = requests.get(url, timeout=10)
        html_grezzo = response.text
        print("Dati grezzi raccolti con successo!")
        print("\n--- Fase 2: Analisi dell'HTML con BeautifulSoup ---")
        soup = BeautifulSoup(html_grezzo, 'html.parser')
        titolo_pagina = soup.find('title').text
        print(f"Il titolo della pagina è: '{titolo_pagina}'")
    
except requests.exceptions.RequestException as e:
        print(f"ERRORE: Impossibile raccogliere i dati. Causa: {e}")