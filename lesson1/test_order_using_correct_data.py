import time
from selenium.webdriver.common.by import By
from conftest import USER_FIRST_NAME
from conftest import USER_LAST_NAME
from conftest import USER_ZIP_CODE
from conftest import CONFIRM_TEXT

def test_add_item_by_card(driver, login_by_standard_user):
    choose_item = driver.find_element(By.CSS_SELECTOR, '#item_0_title_link')
    choose_item.click()

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
    add_to_cart_button.click()

    go_to_cart = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    go_to_cart.click()

    checkout_btn = driver.find_element(By.NAME, 'checkout')
    checkout_btn.click()

    driver.find_element(By.ID, "first-name").send_keys(USER_FIRST_NAME)
    driver.find_element(By.ID, "last-name").send_keys(USER_LAST_NAME)
    driver.find_element(By.ID, "postal-code").send_keys(USER_ZIP_CODE)

    continue_btn = driver.find_element(By.ID, "continue")
    continue_btn.click()

    finish_btn = driver.find_element(By.ID, "finish")
    finish_btn.click()

    confirm_text = driver.find_element(By.XPATH, '//h2[@class = "complete-header"]').text
    assert confirm_text == CONFIRM_TEXT

