from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

def test_filter_lo_hi():
    driver.get("https://www.saucedemo.com/")
    # log, password = request.param
    driver.find_element(By.ID, "user-name").send_keys(f"standard_user")
    driver.find_element(By.ID, "password").send_keys(f"secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    low_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div').text

    select_filter_btn = driver.find_element(By.XPATH, '//span[@class="select_container"]')
    select_filter_btn.click()

    filter_btn_lo_hi = driver.find_element(By.XPATH, '//option[@value="lohi"]')
    filter_btn_lo_hi.click()

    first_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div').text

    assert first_price == low_price

    driver.quit()
