import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_boxplot_male(data,x,y,hue):
    sns.set(rc={'figure.figsize':(80,40)})
    sns.boxplot(data = data, x = x, y=y, hue = hue)
    plt.title("APR of Male Sports by Sport Name", fontsize=50)
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)
    plt.xlabel("Year",fontsize=30)
    plt.ylabel("APR",fontsize=30)
    plt.legend(prop={'size': 40})
    plt.savefig("figs/boxplot_Questino3_male.png")
    plt.close()
    
def generate_boxplot_female(data,x,y,hue):
    sns.set(rc={'figure.figsize':(80,40)})
    sns.boxplot(data = data, x = x, y=y, hue = hue)
    plt.title("APR of Female Sports by Sport Name", fontsize=50)
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)
    plt.xlabel("Year",fontsize=30)
    plt.ylabel("APR",fontsize=40)
    plt.legend(prop={'size': 40})
    plt.savefig("figs/boxplot_Questino3_female.png")
    plt.close()