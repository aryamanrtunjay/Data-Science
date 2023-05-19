import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import dataset as dataset
import dataset
import math
import seaborn as sns

def get_graph():
    crime_ds = dataset.get_dataset()
    vic_race_classes = []
    all_vic_races = []

    for i in range(len(crime_ds)):
        vic_race = crime_ds['SUSP_SEX'][i]
        if vic_race != 'UNKNOWN' and vic_race != "OTHER" and type(vic_race) == str:
            if vic_race not in vic_race_classes:
                vic_race_classes.append(vic_race)
                all_vic_races.append(1)
            else:
                all_vic_races[vic_race_classes.index(vic_race)] += 1

    color_palette = ['#f44336', '#6fa8dc', '#ffd966']
    labels = ["Female", "Male", "Unknown"]
    #all_vic_races.remove(1)
    #vic_race_classes.remove('U') 
    # make font bigger
    plt.rcParams.update({'font.size': 16})
    # make the labels better, make m = male, f = female, u = unknown
    #sns.set_style("darkgrid") 
    plt.rc('axes', titlesize = 18) 
    plt.rc('axes', labelsize = 14)
    plt.rc('xtick', labelsize = 13) 
    plt.rc('ytick', labelsize = 13)
    plt.rc('legend', fontsize =13)
    plt.rc('font', size = 13)
    colors = sns.set_palette(sns.color_palette(color_palette)) 
    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.pie(all_vic_races, labels=labels, autopct='%1.1f%%', colors = colors, radius = 1.5)
    axes.set_title("Suspect Sex in New York City")
    plt.show()
    
get_graph()