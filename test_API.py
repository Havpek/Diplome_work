import requests
import json
from constance import *
import pytest



path_1 = "/contenthub/ajaxgetcontenthubdata?hubtype=freetoplay"
path_2 = "/freelicense/addfreelicense/674005"
path_3 = "/IPlayerService/GetOwnedGames/v0001/?"

 
    
def test_get_info():
        responce = requests.get(Base_URL + "/dynamicstore/userdata/?id=1714906334&cc=RU&v=1&")
        assert responce.json
        assert responce.status_code == 200
    
def test_free_games():
        free_games = {len: id}
        responce = requests.get(Base_URL + path_1, params=free_games)
        assert responce.json()
        assert responce.status_code == 200
    
def test_add_email():
        responce = requests.post(
            Base_URL + "/join/ajaxverifyemail", payload_add_mail)
        assert responce.json()
        assert responce.status_code == 200
    
def test_add_game():
        responce = requests.post(
            Base_URL + path_2, "ajax=true&session\r\nid=5f08c79b7aac7d651c2aa4c2\r\n")
        assert responce.status_code == 200
           
def test_get_list():
    responce = requests.get(
        Special_URL + "/ISteamApps/GetAppList/v2/")
    assert responce.json()
    
def test_get_having_list():
    
    responce = requests.get(
           Special_URL + path_3, "key=04AB93DF9A5678857B0742A66A0C7BDA&steamid=76561198070806378")
    assert responce.json()
    assert responce.status_code == 200