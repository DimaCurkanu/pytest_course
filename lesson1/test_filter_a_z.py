from selenium.webdriver.common.by import By

def test_filter_a_z(driver, login_by_standard_user):

    item_list = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_name')
    items_name = []
    for i in item_list:
        text = i.text
        items_name.append(text)
    expected_result = sorted(items_name)

    select_filter_btn = driver.find_element(By.XPATH, '//span[@class="select_container"]')
    select_filter_btn.click()

    filter_btn_a_z = driver.find_element(By.XPATH, '//option[@value="az"]')
    filter_btn_a_z.click()

    sort_item = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_name')
    actual_result = []
    for i in sort_item:
        text = i.text
        actual_result.append(text)

    assert actual_result == expected_result
