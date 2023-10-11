from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = "https://www.saucedemo.com/"

def test_login_form_user_empty():
    driver = webdriver.Chrome()
    driver.get(url)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    error_message = driver.find_element(By.XPATH, '//h3').text

    time.sleep(5)
    assert error_message == "Epic sadface: Username is required"

    driver.quit()