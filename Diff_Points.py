import pandas as pd
import matplotlib.pyplot as plt
import os

diff_points = pd.DataFrame()
diff_points_xp = pd.DataFrame()

def diff_points(league):

    for league in leagues:
        data = pd.read_csv(os.path.join('data_leagues', league + '.csv'))
        data['forecast_home'] = data['forecast'].apply(lambda x: eval(x))
        data['forecast_away'] = data['forecast'].apply(lambda x: eval(x))
        data['goals'] = data['goals'].apply(lambda x: eval(x))

        data['xP_home'] = data['forecast_home'].apply(lambda f: 3 * float(f['w']) + 1 * float(f['d']))
        data['xP_away'] = data['forecast_away'].apply(lambda f: 3 * float(f['l']) + 1 * float(f['d']))
        data['results'] = data['goals'].apply(lambda f: 3 if float(f['h']) > float(f['a']) else 1 if float(f['h']) == float(f['a']) else 0)
        data['results_away'] = data['goals'].apply(lambda f: 3 if float(f['a']) > float(f['h']) else 1 if float(f['h']) == float(f['a']) else 0)

        results_home = data.groupby('year')['results'].sum()
        results_away = data.groupby('year')['results_away'].sum()
        xp_home = data.groupby('year')['xP_home'].sum()
        xp_away = data.groupby('year')['xP_away'].sum()
        
        df = pd.DataFrame()
        df["diff_points"] = results_home - results_away
        df["diff_points_xp"] = xp_home - xp_away
        df["league"] = league
        df["year"] = df.index
        print(df)



    """
    fig, ax = plt.subplots(figsize=(10, 6))

    colors_points = diff_points.apply(lambda x: "green" if x >= 0 else "red")
    colors_xpoints = diff_points_xp.apply(lambda x: "green" if x >= 0 else "red")

    ax.set_yticks(diff_points.index)
    ax.set_yticklabels(diff_points["year"].astype(str))
    ax.set_xlabel("Différence")
    ax.set_title("Différence Points et xPoints (Home vs Away)")

    ax.barh(diff_points.index - 0.2, diff_points , color=colors_points, height=0.4, label="Diff Points Home/Away")
    ax.barh(diff_points_xp.index + 0.2, diff_points_xp, color=colors_xpoints, height=0.4, label="Diff xPoints Home/Away")
    print(diff_points)
    print(diff_points_xp)"""

leagues = ['La_liga', 'EPL', 'Bundesliga', 'Serie_A', 'RFPL']

diff_points(leagues)