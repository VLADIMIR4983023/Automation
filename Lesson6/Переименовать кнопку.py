from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

search_field = ".form-control"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("SkyPro")

blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, ".btn")))
blue_button.click()

blue_button_text = blue_button.text

print(blue_button_text)

driver.quit()
