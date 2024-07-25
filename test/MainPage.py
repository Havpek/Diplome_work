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
    
    def add_to_cart(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.search_results_filtered_warning'))
            )
        self.browser.find_element(By.CSS_SELECTOR, "a[data-gpnav='item']").click()
        self.browser.find_element(By.CSS_SELECTOR, 'a.btn_green_steamui.btn_medium').click()
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, 'button.DialogButton._DialogLayout.Primary.Focusable')))
        self.browser.find_element(
            By.CSS_SELECTOR, 'button.DialogButton._DialogLayout.Primary.Focusable').click()
        return self.browser.find_element(By.CSS_SELECTOR, "div.pVXX8Pzc4JbT40TP4RwRG").text
    
    def dell_from_cart(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, 'div._33j4SwfO2YH9eI6qV9BKaL.Panel.Focusable')))
        self.browser.find_element(
            By.CSS_SELECTOR, 'div._33j4SwfO2YH9eI6qV9BKaL.Panel.Focusable').click()

        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, 'div._17GFdSD2pc0BquZk5cejg8.Panel.Focusable > div:nth-child(1)'),
                  "Ваша корзина пуста."))
        return self.browser.find_element(
            By.CSS_SELECTOR, 'div._17GFdSD2pc0BquZk5cejg8.Panel.Focusable > div:nth-child(1)').text
