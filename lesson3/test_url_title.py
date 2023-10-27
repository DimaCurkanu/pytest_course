from selenium.webdriver.common.by import By
from lesson3.conftest import LINK, HEADER_TEXT


def test_url_title(driver, wait):
    driver.get(LINK)
    header_text = driver.find_element(By.XPATH,'//h1').text

    assert header_text == HEADER_TEXT

    assert driver.current_url == LINK
