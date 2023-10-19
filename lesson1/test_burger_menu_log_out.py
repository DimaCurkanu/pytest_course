from selenium.webdriver.common.by import By

def test_burger_menu_log_out(driver, login_by_standard_user):

    burger_btn = driver.find_element(By.CSS_SELECTOR, '.bm-burger-button')
    burger_btn.click()

    logout_btn = driver.find_element(By.ID, 'logout_sidebar_link')
    logout_btn.click()

    login_btn = driver.find_element(By.ID, 'login-button')
    value_info = login_btn.get_attribute("value")

    assert value_info == "Login"

    assert login_btn.is_displayed() is True

    driver.quit()