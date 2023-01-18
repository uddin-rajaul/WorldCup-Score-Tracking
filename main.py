import requests
import json
from plyer import notification
import time

url = "https://api.sofascore.com/api/v1/sport/football/events/live"

headers = {
    "authority": "api.sofascore.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.5",
    "cache-control": "max-age=0",
    "if-none-match": "W/^\^7a97b846cd^^",
    "origin": "https://www.sofascore.com",
    "referer": "https://www.sofascore.com/",
    "sec-ch-ua": "^\^Not?A_Brand^^;v=^\^8^^, ^\^Chromium^^;v=^\^108^^, ^\^Brave^^;v=^\^108^^",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "^\^Android^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
}

response = requests.request("GET", url, headers=headers)

jsondata = json.loads(response.text)

for game in jsondata['events']:
    league = game['tournament']['name']
    homeTeam = game['homeTeam']['name']
    awayTeam = game['awayTeam']['name']
    homeScore = game['homeScore']['current']
    awayScore = game['awayScore']['current']
    if league == 'World Cup, Knockout stage':
        while True:
            time.sleep(200)
            icon_path = './world_cup.ico'
            notification.notify(
                title="World Cup Live Score",
                message=league + '|' + homeTeam + " " + str(homeScore) + ' - ' + str(awayScore) + " " + awayTeam,
                app_icon=icon_path,
                # displaying time
                timeout=5
            )




