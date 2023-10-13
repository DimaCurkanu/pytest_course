from selenium.webdriver.common.by import By
import time
from conftest import YOUR_CART_TEXT

def test_open_card_from_picture(driver, login_by_standard_user):
    item_picture = driver.find_element(By.XPATH, '// img[@alt = "Sauce Labs Bike Light"]')
    item_picture.click()
    time.sleep(3)

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
    add_to_cart_button.click()

    go_to_cart = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    go_to_cart.click()
    time.sleep(3)

    yuor_cart = driver.find_element(By.XPATH, '//span[@class = "title"]').text

    assert yuor_cart == YOUR_CART_TEXT

    driver.quit()