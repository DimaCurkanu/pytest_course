from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lesson3.conftest import LINK, driver, wait, LOGIN_TEXT, PASSWORD


def test_login(driver, wait):
    driver.get(LINK)
    start_btn = wait.until(EC.element_to_be_clickable((By.ID, 'startTest')))
    start_btn.click()

    login_field = driver.find_element(By.ID, 'login')
    login_field.send_keys(LOGIN_TEXT)

    pass_field = driver.find_element(By.ID, 'password')
    pass_field.send_keys(PASSWORD)

    agree_box = driver.find_element(By.ID, 'agree')
    agree_box.click()

    register_btn = driver.find_element(By.ID, 'register')
    register_btn.click()

    loader = wait.until(EC.visibility_of_element_located((By.ID, 'loader')))
    assert loader.is_displayed() == True

    success_text = wait.until(EC.visibility_of_element_located((By.ID, 'successMessage'))).text
    assert success_text == 'Вы успешно зарегистрированы!'

