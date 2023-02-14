import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def generate_boxplot(dataframe, x, y):
    sns.set(rc={'figure.figsize':(20,15)})
    sns.boxplot(data = dataframe, x = x, y = y)

    plt.savefig("figs/Boxplot_Question1.png")
    plt.close()
    
def generate_relplot(dataframe, x, y, height, aspect):
    sns.relplot(data = dataframe, x = x, y = y,height=height, aspect=aspect)
    plt.savefig("figs/Relplot_Question1.png")
    plt.close()