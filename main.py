# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 20:54:36 2016

@author: anh
"""

import requests
from datetime import datetime
from pytz import timezone

api_key = "94A80ED45B214C0CB48E4E03D33FAAB9"
user_id = "76561198060322890"

url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={user_id}&format={format}" \
    .format(api_key = api_key, user_id = user_id, format = "json")

r = requests.get(url)

data = r.json()['response']['players'][0]

"http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=XXXXXXXXXXXXXXXXX&steamid=76561197960434622&format=json"

user_lastlogoff = datetime.fromtimestamp(data['lastlogoff'])
user_signup = datetime.fromtimestamp(data['lastlogoff'] - 1000)

if user_lastlogoff > user_signup:
    print "send email"