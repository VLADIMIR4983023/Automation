import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage


@pytest.fixture(scope="module")
def browser():
    # Инициализация браузера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    # Закрытие браузера после завершения всех тестов
    driver.quit()


@pytest.fixture(scope="module")
def fill_form(browser):
    main_page = MainPage(browser)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Заполнение формы
    main_page.first_name("Иван")
    main_page.last_name("Петров")
    main_page.address("Ленина, 55-3")
    main_page.email("test@skypro.com")
    main_page.phone("+7985899998787")
    main_page.zip_code("")
    main_page.city("Москва")
    main_page.country("Россия")
    main_page.job_position("QA")
    main_page.company("SkyPro")
    main_page.send_form()

    # Возврат объекта главной страницы для дальнейших проверок
    return browser


def test_red_element(fill_form):
    result_page = ResultPage(fill_form)
    # Проверка результата на пустой почтовый индекс
    to_be = result_page.empty_zip_result_is_red()

    as_is = 1  # Ожидаемое значение, если почтовый индекс пустой
    assert as_is == to_be


def test_green_elements(fill_form):
    result_page = ResultPage(fill_form)
    # Проверка наличия класса 'alert-success' в других элементах
    classes = result_page.other_elements_result_is_green()
    assert 'alert-success' in classes
