import requests
import json
from constance import *
import pytest

   
def test_get_info():
        responce = requests.get(Base_URL + path_info)
        assert responce.json
        assert responce.status_code == 200
    
def test_free_games():
        free_games = {len: id}
        responce = requests.get(Base_URL + path_free, params=free_games)
        assert responce.json()
        assert responce.status_code == 200
    
def test_add_email():
        responce = requests.post(
            Base_URL + path_mail, payload_add_mail)
        assert responce.json()
        assert responce.status_code == 200
    
def test_add_game():
        responce = requests.post(
            Base_URL + path_add)
        assert responce.status_code == 200
           
def test_get_list():
    responce = requests.get(
        Special_URL + path_list)
    assert responce.json()
    assert responce.status_code == 200
    
def test_get_having_list():
    
    responce = requests.get(
           Special_URL + path_having)
    assert responce.json()
    assert responce.status_code == 200