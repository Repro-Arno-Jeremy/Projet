import requests
from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd

def scrapping(league = "La_liga", year="2024") :
    # URL de la page que vous voulez scraper
    url = f"https://understat.com/league/{league}/{year}"  # Exemple pour la Premier League (EPL)

    # Récupérer le contenu de la page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # Recherche des balises script contenant "statData"
    datas = [] # Liste pour stocker les données, potentiellement plusieurs donc tableau
    for script in soup.find_all("script"):
        if script.string and "datesData" in script.string:
            datas.append(script.string)

    data = datas[0]
    decoded_data = bytes(data, "utf-8").decode("unicode_escape")
    begin = decoded_data.find("'") + 1
    end = decoded_data.rfind("'")
    data_json = decoded_data[begin:end]
    return data_json

def data_sorted(league):
    dict_league = pd.DataFrame()
    for i in range(2014, 2024):
        decoded_data = scrapping(league, str(i))
        dataframe = pd.read_json(StringIO(decoded_data)).drop('datetime', axis = 1)
        dataframe = dataframe.assign(year = i)
        dict_league = pd.concat([dict_league, dataframe])
    return dict_league

data_sorted_result = data_sorted('La_liga')


if data_sorted_result is not None:
    csv_file_path = "la_liga_data.csv" 
    data_sorted_result.to_csv(csv_file_path)
    print(f"Data successfully exported to {csv_file_path}")