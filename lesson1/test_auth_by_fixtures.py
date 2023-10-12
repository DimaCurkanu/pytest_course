import time
from conftest import INVENTORYLINK


def test_login_form(driver, login_by_standard_user):
    time.sleep(3)
    assert driver.current_url == INVENTORYLINK

    driver.quit()