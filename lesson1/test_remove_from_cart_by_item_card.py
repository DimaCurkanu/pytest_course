import time
from selenium.webdriver.common.by import By

def test_delete_item_from_cart(driver, login_by_standard_user):
    choose_item = driver.find_element(By.CSS_SELECTOR, '#item_0_title_link')
    choose_item.click()
    time.sleep(3)

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
    add_to_cart_button.click()

    go_to_cart = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    go_to_cart.click()

    item = driver.find_element(By.CLASS_NAME, 'cart_item')
    remove_button = driver.find_element(By.NAME, 'remove-sauce-labs-bike-light')
    remove_button.click()
    time.sleep(3)

    assert item.is_displayed() is False

    driver.quit()