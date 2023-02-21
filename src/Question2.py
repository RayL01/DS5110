import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_lineplot(data, x, y, hue):
    sns.boxplot(data = data, x = x, y = y, hue = hue)
    plt.savefig("figs/Boxplot_Questino2.png")
    plt.close()