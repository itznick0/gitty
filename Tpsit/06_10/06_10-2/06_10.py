from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("file:///C:/Users/admin/Desktop/Informatica 2025/Tpsit/06_10/06_10-1/06_10.html")

    wait = WebDriverWait(driver, 10)

    binary_numbers_to_test = [
        "0000", "0001", "0010", "0011",
        "0100", "0101", "0110", "0111",
        "1000", "1001", "1010", "1011",
        "1100", "1101", "1110", "1111"
    ]

    passed = 0
    total = len(binary_numbers_to_test)

    for i in range(len(binary_numbers_to_test)):
        binary = binary_numbers_to_test[i]

        print(f"\n{binary} (Test: {i})")

        bit_boxes = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "bit-box")))

        for j in range(4):
            current_bit = binary[j]
            if current_bit == '1':
                target_bit = '1'
            else:
                target_bit = '0'
            
            if bit_boxes[j].text != target_bit:
                bit_boxes[j].click()

        calculate_btn = driver.find_element(By.ID, "calculateBtn")
        calculate_btn.click()

        result_element = wait.until(EC.presence_of_element_located((By.ID, "result")))
        result_text = result_element.text

        expected_text = f"Risultato: {i}"

        if result_text == expected_text:
            print(f"Corretto: '{binary}' - risultato: {i}")
            passed += 1
        else:
            print(f"Errato: Atteso '{expected_text}' - trovato '{result_text}'")

    print(f"\nRisultato: {passed}/{total} passati")

finally:
    print("\nOperazione completata. Chiudo il browser.")
    driver.quit()