from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")
button = driver.find_element(By.CSS_SELECTOR, ".btn").click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "p.bg-success")))
green_box_text = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(green_box_text)

driver.quit()
