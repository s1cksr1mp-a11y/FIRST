from selenium import webdriver
from selenium.webdriver.common.by import By
import time








def test_open_s6(browser):
    browser.get("https://baserock.pro/")
    for i in range(0, 10000, 500):  # Скроллим с шагом 500 пикселей
        browser.execute_script(f"window.scrollTo(0, {i});")
        time.sleep(0.3)

    policy_link = browser.find_element(By.XPATH, value= '//a[text()="Политика конфиденциальности"]')
    time.sleep(1)
    policy_link.click()


    time.sleep(2)
    policy = browser.find_elements(By.XPATH, '//*[contains(@class, "navItem")]')
    assert len(policy) == 4
