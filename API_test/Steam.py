import requests
import json
from constance import *

class Base:
    def __init__(self, url_1=Base_URL):
        self.url_1 = url_1
    
    def get_info(self):
        responce = requests.get(self.url_1)
        return responce