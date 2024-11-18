import pandas as pd
import matplotlib.pyplot as plt

#data = pd.read_csv("la_liga_data.csv")
#data['year'] = data['year'].astype(int).apply(lambda x: f"{str(x)[-2:]}-{str(x + 1)[-2:]}")
#data = data.set_index(["year"])  # On remet les index multi-niveaux

#annees_uniques = data.index.get_level_values('year').unique().to_list()

""" def create_graph1(): 
    parameters = ["xG"]
    fig, ax = plt.subplots()
    plt.title("La_liga")
    for parameter in parameters:             
        ax.plot(annees_uniques, mean_value(parameter), color="orange")
        ax.scatter(annees_uniques, mean_value(parameter), color="orange", marker="o", label="Points individuels")
    plt.ylabel("Mean gained points per match")
    plt.show()

def mean_value(parameter):
    values = []
    for annee in annees_uniques:
        values.append(data.loc[annee].mean()[parameter])
    return values """

# Charger les données
data = pd.read_csv('la_liga_data.csv')

# Extraire les valeurs xG de domicile et extérieur en les convertissant en type numérique
#data['xG_home'] = data['xG'].apply(lambda x: eval(x)['h']).astype(float)
#data['xG_away'] = data['xG'].apply(lambda x: eval(x)['a']).astype(float)

# Extraire les probabilités de forecast
data['forecast_home'] = data['forecast'].apply(lambda x: eval(x))
data['forecast_away'] = data['forecast'].apply(lambda x: eval(x))

# Calculer les points attendus (xP) pour domicile et extérieur
data['xP_home'] = data['forecast_home'].apply(lambda f: 3 * float(f['w']) + 1 * float(f['d']))
data['xP_away'] = data['forecast_away'].apply(lambda f: 3 * float(f['l']) + 1 * float(f['d']))

# Calculer la moyenne de xG pour les équipes à domicile et à l'extérieur pour chaque saison
#average_xG_home = data.groupby('year')['xG_home'].mean()
#average_xG_away = data.groupby('year')['xG_away'].mean()

# Calculer la moyenne de xP pour les équipes à domicile et à l'extérieur par saison
average_xP_home = data.groupby('year')['xP_home'].mean()
average_xP_away = data.groupby('year')['xP_away'].mean()

# Affichage des résultats
#for year in average_xG_home.index:
#    print(f"Saison {year} - xG moyen domicile : {average_xG_home[year]:.2f}, xG moyen extérieur : {average_xG_away[year]:.2f}")

def create_graph():
    fig, ax = plt.subplots()
    plt.title("La_liga")
    ax.plot(average_xP_home.index, average_xP_home, color="orange", label="xP_home")
    ax.scatter(average_xP_home.index, average_xP_home, color="orange", marker="o", label="xP_home")
    ax.plot(average_xP_away.index, average_xP_away, color="red", label="xP_away")
    ax.scatter(average_xP_away.index, average_xP_away, color="red", marker="o", label="xP_away")

    plt.ylabel("Mean gained points per match")
    plt.show()

create_graph()