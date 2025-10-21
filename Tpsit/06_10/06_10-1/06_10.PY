from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("file:///C:/Users/admin/Desktop/Informatica 2025/Tpsit/06_10/06_10-1/06_10.html")

    wait = WebDriverWait(driver, 10)

    bit_boxes = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "bit-box")))

    bit_boxes[1].click()
    bit_boxes[2].click()

    calculate_btn = driver.find_element(By.ID, "calculateBtn")
    calculate_btn.click()

    result_element = wait.until(EC.presence_of_element_located((By.ID, "result")))
    testo_del_messaggio = result_element.text

    print(testo_del_messaggio)

    if testo_del_messaggio == "Risultato: 6":
        print("Test POSITIVO: Il valore è corretto.")
    else:
        print(f"Test NEGATIVO: Il valore atteso era '6', ma è stato trovato '{testo_del_messaggio}'")

finally:
    print("Operazione completata. Chiudo il browser.")
    driver.quit()