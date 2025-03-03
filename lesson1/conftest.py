import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = 'https://www.saucedemo.com/'
INVENTORYLINK = "https://www.saucedemo.com/inventory.html"

ADD_TO_CART_TEXT = "Add to cart"
YOUR_CART_TEXT = "Your Cart"
USER_FIRST_NAME = "John"
USER_LAST_NAME = "Dow"
USER_ZIP_CODE = "78600"
CONFIRM_TEXT = "Thank you for your order!"

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def login_by_standard_user(driver):#request попробовать делать через
    driver.get("https://www.saucedemo.com/")
    # log, password = request.param
    driver.find_element(By.ID, "user-name").send_keys(f"standard_user")
    driver.find_element(By.ID, "password").send_keys(f"secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    yield driver