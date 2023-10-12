import time
from selenium.webdriver.common.by import By

def test_add_item_by_card(driver, login_by_standard_user):

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-bike-light')
    add_to_cart_button.click()
    time.sleep(2)

    go_to_cart = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    go_to_cart.click()
    # time.sleep(3)

    check_cart_text = driver.find_element(By.ID, 'item_0_title_link').text
    assert check_cart_text == "Sauce Labs Bike Light"