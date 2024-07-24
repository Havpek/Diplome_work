from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from constants import Submit_URL
from data import *

class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(Submit_URL)
    
    def filling_in_the_fields(self, username, password):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
        )
        self.browser.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(username)
        self.browser.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
    
    def click_submit_button(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.DjSvCZoKKfoNSmarsEcTS'))
        )
        self.browser.find_element(By.CSS_SELECTOR, 'button.DjSvCZoKKfoNSmarsEcTS').click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span.pulldown.global_action_link.persona_name_text_content'))
        )
        return self.browser.find_element(By.CSS_SELECTOR, 'span.pulldown.global_action_link.persona_name_text_content').text