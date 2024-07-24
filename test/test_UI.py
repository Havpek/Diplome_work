from MainPage import MainPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data import *

def test_assertion(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.filling_in_the_fields('testingfechures', '553085530855308g')
    user = main_page.click_submit_button()
    assert user == 'test250995'