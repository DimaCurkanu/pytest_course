from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_login_form():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    # time.sleep(3)

    choose_item = driver.find_element(By.CSS_SELECTOR, '#item_0_title_link')
    choose_item.click()
    # time.sleep(3)

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-bike-light')
    add_to_cart_button.click()
    # time.sleep(3)

    go_to_cart = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    go_to_cart.click()
    # time.sleep(3)

    check_cart_text = driver.find_element(By.ID, 'item_0_title_link').text
    # print(check_cart_text)
    assert check_cart_text == "Sauce Labs Bike Light"