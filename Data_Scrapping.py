import requests
from bs4 import BeautifulSoup
import json
import re

# URL de la page que vous voulez scraper
url = "https://understat.com/"  # Exemple pour la Premier League (EPL)

# Récupérer le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Recherche des balises script contenant "statData"
datas = []
for script in soup.find_all("script"):
    if script.string and "statData" in script.string:
        datas.append(script.string)

#print(datas)

datas = datas[0].split("var")[1].split("= JSON.parse('")[1].split("');")[0]
decoded_data = bytes(datas, "utf-8").decode("unicode_escape")
decoded_data = json.loads(decoded_data)

dictionary_leagues = {}

for data in decoded_data:
    if 'league_id' in data:
        del data['league_id']

    if data['league'] not in dictionary_leagues:
        dictionary_leagues[data['league']] = [data]
    else:
        dictionary_leagues[data['league']].append(data)

print(dictionary_leagues['La liga'])

'''
# Analyser et afficher les données des buts par match
for player in data:
    player_name = player['player_name']
    avg_goals = player.get('goals') / player.get('games', 1) if player.get('games') else 0
    print(f"{player_name}: {avg_goals:.2f} buts par match")
'''