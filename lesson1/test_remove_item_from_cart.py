import time
from selenium.webdriver.common.by import By
from conftest import ADD_TO_CART_TEXT

def test_delete_item_from_cart(driver, login_by_standard_user):

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
    add_to_cart_button.click()

    cart_badge = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]').text

    assert cart_badge == '1'

    remove_button = driver.find_element(By.NAME, 'remove-sauce-labs-bike-light')
    remove_button.click()
    time.sleep(3)

    add_to_cart_button_text = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light').text

    assert add_to_cart_button_text == ADD_TO_CART_TEXT

    driver.quit()