from selenium.webdriver.common.by import By
import time

def test_filter_a_z(driver, login_by_standard_user):
    first_item = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text

    select_filter_btn = driver.find_element(By.XPATH, '//span[@class="select_container"]')
    select_filter_btn.click()

    filter_btn_z_a = driver.find_element(By.XPATH, '//option[@value="za"]')
    filter_btn_z_a.click()
    time.sleep(3)

    sort_item = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text

    assert sort_item != first_item

    driver.quit()