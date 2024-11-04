import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("la_liga_data.csv")

def create_graph(): 
    fig, ax = plt.subplots()             
    ax.plot( ["14-15", "15-16", "16-17", "17-18", "18-19", "19-20", "20-21"], [1, 2, 3, 4, 5, 6, 7])
    plt.show()                           
    return 0

create_graph()