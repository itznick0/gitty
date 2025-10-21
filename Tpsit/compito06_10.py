import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("file:///C:/Users/admin/Documents/Multi programma java/index-conversione.html")

    # Cerca il bottone con ID 'mioBottone'
    print("Sto per cliccare il bottone...")
    bottone = driver.find_element(By.ID, "mioBottone")
    bottone.click()
    print("Bottone cliccato! Ora aspetto il messaggio...")

    # Usa WebDriverWait per aspettare che l'elemento con ID 'messaggio' diventi visibile
    wait = WebDriverWait(driver, 10)
    elemento_messaggio = wait.until(
        EC.visibility_of_element_located((By.ID, "messaggio"))
    )

    # Legge il testo del messaggio
    testo_del_messaggio = elemento_messaggio.text
    print(f"Messaggio ricevuto: {testo_del_messaggio}")

except Exception as e:
    print(f"Errore: {e}")

finally:
    driver.quit()