from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button(browser):
    browser.get(link)
    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket") != [], "There is no button"
    time.sleep(20)
