import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd

def scrapping() :

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
    #decoded_data = json.loads(decoded_data)
    return decoded_data

def data_sorted(decoded_data, league) :
    dict = pd.read_json(decoded_data)

    dict = dict.drop('league_id', axis=1)
    dict = dict.set_index(['league', 'year', 'month'])
    return dict.loc[league]

decoded_data = scrapping()
data_sorted_result = data_sorted(decoded_data, 'La liga')

if data_sorted_result is not None:
    csv_file_path = "la_liga_data.csv" 
    data_sorted_result.to_csv(csv_file_path)
    print(f"Data successfully exported to {csv_file_path}")
