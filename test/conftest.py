import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def chrome_browser():
    chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome.maximize_window()
    yield chrome
    chrome.quit()