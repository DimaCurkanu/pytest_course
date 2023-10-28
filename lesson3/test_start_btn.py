from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lesson3.conftest import LINK, driver, wait


def test_url_wait(driver, wait):
    driver.get(LINK)
    start_btn = wait.until(EC.element_to_be_clickable((By.ID, 'startTest')))

    assert start_btn.is_enabled() == True
