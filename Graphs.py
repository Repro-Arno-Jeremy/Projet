import pandas as pd
import matplotlib.pyplot as plt

# Charger les données

def create_graph(league):
    data = pd.read_csv(league + '.csv')

    # Extraire les probabilités de forecast
    data['forecast_home'] = data['forecast'].apply(lambda x: eval(x))
    data['forecast_away'] = data['forecast'].apply(lambda x: eval(x))
    data['goals'] = data['goals'].apply(lambda x: eval(x))

    # Calculer les points attendus (xP) pour domicile et extérieur
    data['xP_home'] = data['forecast_home'].apply(lambda f: 3 * float(f['w']) + 1 * float(f['d']))
    data['xP_away'] = data['forecast_away'].apply(lambda f: 3 * float(f['l']) + 1 * float(f['d']))
    data['results'] = data['goals'].apply(lambda f: 3 if float(f['h']) > float(f['a']) else 1 if float(f['h']) == float(f['a']) else 0)
    data['results_away'] = data['goals'].apply(lambda f: 3 if float(f['a']) > float(f['h']) else 1 if float(f['h']) == float(f['a']) else 0)


    # Calculer la moyenne de xP pour les équipes à domicile et à l'extérieur par saison
    average_xP_home = data.groupby('year')['xP_home'].mean()
    average_xP_away = data.groupby('year')['xP_away'].mean()
    average_results = data.groupby('year')['results'].mean()
    average_results_away = data.groupby('year')['results_away'].mean()

    #Création graphe
    fig, ax = plt.subplots()
    plt.title(league)
    ax.plot(average_xP_home.index, average_xP_home, color="orange", label="xP_home")
    ax.scatter(average_xP_home.index, average_xP_home, color="orange", marker="o")
    ax.plot(average_xP_away.index, average_xP_away, color="red", label="xP_away")
    ax.scatter(average_xP_away.index, average_xP_away, color="red", marker="o")
    ax.plot(average_results.index, average_results, color="blue", label="results")
    ax.scatter(average_results.index, average_results, color="blue", marker="o")
    ax.plot(average_results_away.index, average_results_away, color="green", label="results_away")
    ax.scatter(average_results_away.index, average_results_away, color="green", marker="o")

    plt.ylabel("Mean gained points per match")
    plt.legend(fontsize=10)
    plt.show()


leagues = ['La_liga', 'EPL', 'Bundesliga', 'Serie_A', 'Ligue_1', 'RFPL']

create_graph(leagues[1])