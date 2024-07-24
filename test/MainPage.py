from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from constants import Submit_URL
from data import *

class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(Submit_URL)
    
    def find_fields(self):
        self._userName = (By.NAME, "text")
        self._passsword = (By.NAME, "password")
    
    def filling_in_the_fields(self):
        self.browser.find_element(*self._userName).send_keys(userName)
        self.browser.find_element(*self._passsword).send_keys(password)
    
    def click_submit_button(self):
        WebDriverWait(self.browser, 120, 0,1).until(EC.element_to_be_clickable(self._button)).click()