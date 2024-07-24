import pytest
import requests
import json
from Steam import Base, Special

base = Base
special = Special

def Test_Steam():
    info = base.get_info
    assert info.status_code == 200

    