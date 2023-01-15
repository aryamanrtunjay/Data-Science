import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import dataset as dataset
import dataset
import math

def get_graph():
    crime_ds = dataset.get_dataset()
    vic_race_classes = []
    all_vic_races = []

    for i in range(len(crime_ds)):
        vic_race = crime_ds['VIC_RACE'][i]
        if vic_race != 'UNKNOWN' and vic_race != "OTHER" and type(vic_race) == str:
            if vic_race not in vic_race_classes:
                vic_race_classes.append(vic_race)
                all_vic_races.append(1)
            else:
                all_vic_races[vic_race_classes.index(vic_race)] += 1


    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.pie(all_vic_races, labels=vic_race_classes, autopct='%1.1f%%')
    plt.show()