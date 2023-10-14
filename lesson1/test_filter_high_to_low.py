from selenium.webdriver.common.by import By

def test_filter_hi_lo(driver, login_by_standard_user):
    high_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div').text

    select_filter_btn = driver.find_element(By.XPATH, '//span[@class="select_container"]')
    select_filter_btn.click()

    filter_btn_lo_hi = driver.find_element(By.XPATH, '//option[@value="hilo"]')
    filter_btn_lo_hi.click()

    first_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div').text

    assert first_price == high_price

    driver.quit()