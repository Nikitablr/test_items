import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_have_button(browser):
    browser.get(link)
    time.sleep(20)
    button=browser.find_element(By.CSS_SELECTOR, (".btn-add-to-basket"))
    assert button.text == "Añadir al carrito"