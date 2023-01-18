import json

with open('live_score.json') as f:
    jsondata = json.load(f)


league = jsondata['events'][0]['tournament']['name']

homeTeam = jsondata['events'][0]['homeTeam']['name']
awayTeam = jsondata['events'][0]['awayTeam']['name']

homeScore = jsondata['events'][0]['homeScore']['current']
awayScore = jsondata['events'][0]['awayScore']['current']

# print(league, '|', homeTeam, homeScore, '-', awayScore, awayTeam)


for game in jsondata['events']:
    league = game['tournament']['name']
    homeTeam = game['homeTeam']['name']
    awayTeam = game['awayTeam']['name']
    homeScore = game['homeScore']['current']
    awayScore = game['awayScore']['current']
    if league == 'World Cup, Knockout stage':
        print(league, '|', homeTeam, homeScore, '-', awayScore, awayTeam)

