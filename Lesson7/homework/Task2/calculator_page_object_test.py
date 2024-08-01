from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_result():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()
                                               ))
    main_page = MainPage(browser)

    # Задержка, если она необходима
    main_page.delay("45")
    # Выполнение операций калькулятора
    main_page.click_button("7")
    main_page.click_button("+")
    main_page.click_button("8")
    main_page.click_button("=")
    # Ожидание исчезновения спиннера загрузки
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element((By.CSS_SELECTOR, ".spinner-class"))
    # Замените на действительный селектор спиннера
    )

    result_page = ResultPage(browser)
    result = result_page.display_time_result()

    # Здесь лучше проверять результат по какому-то критерию
    # например, если ожидаемый результат был 15, то можно проверить это
    expected_result = 15  # Замените на переменную, если значение будет динамическим
    assert expected_result == result, f"Expected {expected_result}, but got {result}"

    browser.quit()
