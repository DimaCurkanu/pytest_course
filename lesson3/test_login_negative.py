from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lesson3.conftest import LINK, driver, wait, LOGIN_TEXT, PASSWORD, ALERT_TEXT


def test_login(driver, wait):
    driver.get(LINK)
    start_btn = wait.until(EC.element_to_be_clickable((By.ID, 'startTest')))
    start_btn.click()

    login_field = driver.find_element(By.ID, 'login')
    login_field.send_keys(LOGIN_TEXT)

    # empty Password field =======>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    pass_field = driver.find_element(By.ID, 'password')
    pass_field.send_keys('')

    agree_box = driver.find_element(By.ID, 'agree')
    agree_box.click()

    register_btn = driver.find_element(By.ID, 'register')
    register_btn.click()

    alert = wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == ALERT_TEXT
    alert.accept()



