import requests
import json
from constance import *


path_1 = "/contenthub/ajaxgetcontenthubdata?hubtype=freetoplay"
path_2 = "/freelicense/addfreelicense/21350"
path_3 = "/IPlayerService/GetOwnedGames/v0001/?key=Token&steamid=Steam_ID"

class Base:
    def __init__(self, url_1=Base_URL):
        self.url_1 = url_1
    
    def get_info(self):
        responce = requests.get(self.url_1)
        return responce.json()
    
    def free_games(self, id: int):
        free_games = {id: free_games}
        responce = requests.get(self.url_1 + path_1, params=free_games)
        return responce.json()
    
    def add_email(self, email: str, body: str):
        mail = {email: mail}
        responce = requests.post(
            self.url_1 + "/join/ajaxverifyemail", params=mail, json=body)
        return responce.json()
    
    def add_game(self, game_id: id, body: str):
        game_id = {id: game_id}
        responce = requests.post(
            self.url_1 + path_2, params=game_id, json=body)
        return responce.json()

class Special:
    def __init__(self, url_2=Special_URL):
        self.url_2 = url_2
    
    def get_list(self, appid: int):
        games = {appid: games}
        responce = requests.get(
            self.url_2 + "/ISteamApps/GetAppList/v2/",
              params=games)
        return responce.json()
    
    def get_having_list(self, appid: int):
        params = {appid: games}
        responce = requests.get(self.url_2 + path_3, params=params)
        return responce.json()