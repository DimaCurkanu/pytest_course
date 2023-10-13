from selenium.webdriver.common.by import By
import time

def test_open_card_from_picture(driver, login_by_standard_user):
    item_picture = driver.find_element(By.XPATH, '//img[@alt = "Sauce Labs Fleece Jacket"]')
    item_picture.click()
    time.sleep(1)

    card_picture = driver.find_element(By.XPATH, '//img[@alt = "Sauce Labs Fleece Jacket"]')

    assert card_picture.is_displayed()

    driver.quit()