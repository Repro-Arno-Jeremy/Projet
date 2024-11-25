import requests
from io import StringIO
import pandas as pd
import os

def scrapping(league_initial, year="2021") :
    # URL de la page que vous voulez scraper
    url = f"https://www.football-data.co.uk/mmz4281/{year}/{league_initial}1.csv"  # Exemple pour la Premier League (EPL)

    # Récupérer le contenu de la page
    response = requests.get(url)
    if response.status_code == 200:
        # 2. Charger les données dans un DataFrame avec pandas
        csv_data = StringIO(response.text)  # Convertir le contenu en objet StringIO
        df = pd.read_csv(csv_data)  # Lire directement depuis StringIO
        return df

def data_sorted(league):
    dict_league = pd.DataFrame()
    for i in range(14, 24):
        end = i + 1  # La deuxième partie est toujours +1
        year = int(f"{i}{end}")  # Crée le nombre en concaténant
        dataframe = scrapping(league, year)
        dataframe = dataframe.dropna(how = 'all')
        dataframe = dataframe[dataframe['FTR'].notna()]
        dataframe = dataframe.assign(year = i)
        dict_league = pd.concat([dict_league, dataframe])
    return dict_league

leagues = ['T1','G1', 'N1', 'B1', 'P1']

# G1 Pas tout à fait correct dans les données sauvegardées, peut manquer résultats -> matchs annulés ?

for league in leagues:
    data_sorted_result = data_sorted(league)
    if data_sorted_result is not None:
        csv_file_path = os.path.join('other_data_leagues', league + ".csv") 
        data_sorted_result.to_csv(csv_file_path)
        print(f"Data successfully exported to {csv_file_path}")