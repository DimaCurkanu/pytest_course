from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lesson3.conftest import LINK, driver, wait, LOGIN_TEXT, PASSWORD, SUCCESS_TEXT


def test_login(driver, wait):
    driver.get(LINK)
    start_btn = wait.until(EC.element_to_be_clickable((By.ID, 'startTest')))
    start_btn.click()

    login_field = driver.find_element(By.ID, 'login')
    login_field.clear()
    login_field.send_keys(LOGIN_TEXT)

    pass_field = driver.find_element(By.ID, 'password')
    pass_field.clear()
    pass_field.send_keys(PASSWORD)

    agree_box = driver.find_element(By.ID, 'agree')
    agree_box.click()
    # # Returns height, width, x and y coordinates referenced element
    # res = driver.find_element(By.ID, 'agree').rect
    # print(res)

    assert agree_box.is_selected() == True

    register_btn = driver.find_element(By.ID, 'register')
    register_btn.click()

    loader = wait.until(EC.visibility_of_element_located((By.ID, 'loader')))
    loader_res = driver.find_element(By.ID, 'loader').rect
    print(loader_res)
    assert loader.is_displayed() == True

    success_text = wait.until(EC.visibility_of_element_located((By.ID, 'successMessage'))).text
    assert success_text == SUCCESS_TEXT

