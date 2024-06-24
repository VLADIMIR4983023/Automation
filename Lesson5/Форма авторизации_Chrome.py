from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/login")

# Введите значение "tomsmith" в поле "username"
username_locator = "#username"
username_input = driver.find_element(By.CSS_SELECTOR, username_locator)
username_input.send_keys("tomsmith")

# Введите значение "SuperSecretPassword!" в поле "password"
password_locator = "#password"
password_input = driver.find_element(By.CSS_SELECTOR, password_locator)
password_input.send_keys("SuperSecretPassword!")

# Нажмите кнопку "Login"
button = driver.find_element(By.CSS_SELECTOR, ".radius")
button.click()

sleep(5)
driver.quit()
