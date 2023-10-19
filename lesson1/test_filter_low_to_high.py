import time

from selenium.webdriver.common.by import By

def test_filter_hi_lo(driver, login_by_standard_user):

    low_price = driver.find_element(By.CSS_SELECTOR, '#inventory_container > div > div:nth-child(5) > div.inventory_item_description > div.pricebar > div').text

    select_filter_btn = driver.find_element(By.XPATH, '//span[@class="select_container"]')
    select_filter_btn.click()

    filter_btn_lo_hi = driver.find_element(By.XPATH, '//option[@value="lohi"]')
    filter_btn_lo_hi.click()

    first_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div').text

    assert first_price == low_price

    driver.quit()