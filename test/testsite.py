from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest







def test_open_s6(browser):
    browser.get("https://abcex.io/")
    office_link = browser.find_element(By.XPATH, value= '//a[text()="Офисы"]')
    office_link.click()
    title =  title = browser.find_element(By.XPATH, "//*[contains(text(), 'Адреса партнерских офисов ABCEX')]")
    assert title.text == 'Адреса партнерских офисов ABCEX'

