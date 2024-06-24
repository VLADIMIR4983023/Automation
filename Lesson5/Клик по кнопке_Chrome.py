from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(
)))
"""Клик по кнопке"""
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
search_lokator = "button"
search_lokator2 = "button.added-manually"
for _ in range(5):
    add_button = driver.find_element(By.CSS_SELECTOR, search_lokator)
    add_button.click()
sleep(3)

delete_buttons = driver.find_elements(By.CSS_SELECTOR, search_lokator2)
print("Количество кнопок 'Delete':", len(delete_buttons))

driver.quit()


sleep(3)
