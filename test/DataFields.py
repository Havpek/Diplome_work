from selenium.webdriver.common.by import By

class DataFild():
    def __init__(self, browser):
        self.browser = browser
    

    def find_fields(self):
        self.class_userName= (By.CLASS_NAME, "_2GBWeup5cttgbTw8FM3tfx")
        self.class_password = (By.CLASS_NAME, "_2GBWeup5cttgbTw8FM3tfx")
    
    def get_class_userName(self):
        return self.browser.find_element(*self.class_userName).get_attribute("class")
    
    def get_class_password(self):
        return self.browser.find_element(*self.class_password).get_attribute("class")
    
    