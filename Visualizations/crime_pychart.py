import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import dataset as dataset
import dataset as dataset
import seaborn as sns

def get_graph():
    crime_ds = dataset.get_dataset()
    crime_desc_classes = []
    all_crime_descs = []

    for i in range(len(crime_ds)):
        crime_type = crime_ds['LAW_CAT_CD'][i]
        if crime_type == 'FELONY' :
            crime_desc = crime_ds['OFNS_DESC'][i]
            if(crime_desc not in crime_desc_classes):
                crime_desc_classes.append(crime_desc)
                all_crime_descs.append(1)
            else:
                all_crime_descs[crime_desc_classes.index(crime_desc)] += 1
    #increase the font size 
    plt.rcParams.update({'font.size': 12})
    cleaned_crime_descs = []
    cleaned_crime_desc_classes = []
    for i in all_crime_descs:
        if i / sum(all_crime_descs) > 0.009:
            cleaned_crime_descs.append(i)
            cleaned_crime_desc_classes.append(crime_desc_classes[all_crime_descs.index(i)])
        else:
            if("OTHER" not in cleaned_crime_desc_classes):
                cleaned_crime_desc_classes.append("OTHER")
                cleaned_crime_descs.append(i)
            else:
                cleaned_crime_descs[cleaned_crime_desc_classes.index("OTHER")] += i
    r = cleaned_crime_desc_classes.index("RAPE") 
    cleaned_crime_desc_classes.pop(r)
    cleaned_crime_descs.pop(r)
    o = cleaned_crime_desc_classes.index("OTHER")
    cleaned_crime_desc_classes.pop(o)
    cleaned_crime_descs.pop(o)
    k = cleaned_crime_desc_classes.index("SEX CRIMES")
    cleaned_crime_desc_classes.pop(k)
    cleaned_crime_descs.pop(k)
    # k = cleaned_crime_desc_classes.index("SEX CRIMES")
    # cleaned_crime_descs[k] = 0
    # set it blank
    plt.rc('axes', titlesize = 23) 
    plt.rc('axes', labelsize = 26)
    plt.rc('xtick', labelsize = 22) 
    plt.rc('ytick', labelsize = 22)
    plt.rc('legend', fontsize = 23)
    plt.rc('font', size = 25)
    #pdb.set_trace()
    color_palette = ['#f44336', '#6fa8dc', '#ffd966', '#b6d7a8']
    colors = sns.set_palette(sns.color_palette(color_palette)) 

    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.pie(cleaned_crime_descs, labels=cleaned_crime_desc_classes, autopct='%1.1f%%', colors=colors, radius = 1.5)

    plt.show()


get_graph()

#%%
