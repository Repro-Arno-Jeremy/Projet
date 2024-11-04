import requests
from bs4 import BeautifulSoup
import json
import re

# URL de la page que vous voulez scraper
url = "https://understat.com/"  # Exemple pour la Premier League (EPL)

# Récupérer le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

print(soup)

# Trouver le script contenant les données JSON
scripts = soup.find_all("script")
for script in scripts:
    if "playersData" in script.text:
        # Extraire les données JSON en utilisant une expression régulière
        json_text = re.search(r"var playersData = (\[.*?\]);", script.string)
        if json_text:
            data = json.loads(json_text.group(1))
            break

# Analyser et afficher les données des buts par match
for player in data:
    player_name = player['player_name']
    avg_goals = player.get('goals') / player.get('games', 1) if player.get('games') else 0
    print(f"{player_name}: {avg_goals:.2f} buts par match")
