import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

LINK = 'https://victoretc.github.io/selenium_waits/'

HEADER_TEXT = 'Практика с ожиданиями в Selenium'
LOGIN_TEXT = 'Dima Curkanu'
PASSWORD = '12345678'
SUCCESS_TEXT = 'Вы успешно зарегистрированы!'

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait

