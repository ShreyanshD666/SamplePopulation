import statistics as st
import pandas as pd
import plotly.figure_factory as ff
import random

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()

populationMean = st.mean(data)

print("The population mean is:", populationMean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

def plot_graph(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["claps"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(10)
        mean_list.append(set_of_means)
    plot_graph(mean_list)
    sampleMean = st.mean(mean_list)
    print("The sample mean is:", sampleMean)

setup()