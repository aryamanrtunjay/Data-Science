import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
import pdb
import dataset as dataset
import seaborn as sns

def get_graph():
    # Get the dataset
    crime_ds = dataset.get_dataset()

    # Get the time data
    times_raw = [i for i in crime_ds['CMPLNT_FR_DT'] if type(i) != float]
    # Get the hour of each time
    all_times = []
    for i in range(len(times_raw)):
        all_times.append(int(times_raw[i][0:2]))

    # Get the number of crimes for each hour
    time_data = [0 for i in range(12)]

    for i in all_times:
        time_data[i - 1] += 1

    # Set up the graph
    fig = plt.figure()
    axes = fig.add_subplot(111)

    # Set the x-axis labels
    time_values = np.arange(1, 13, 1)
    timevaluemonths = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Plot the data
    axes.bar(time_values, time_data)

    plt.rc('axes', titlesize = 18) 
    plt.rc('axes', labelsize = 14)
    plt.rc('xtick', labelsize = 13) 
    plt.rc('ytick', labelsize = 13)
    plt.rc('legend', fontsize =13)
    plt.rc('font', size = 13)
    color_palette = ['#f44336', '#6fa8dc', '#ffd966', '#b6d7a8']
    colors = sns.set_palette(sns.color_palette(color_palette)) 

    # Configure the graph
    axes.set_xlabel('Time of Day')
    axes.set_ylabel('Number of Crimes')
    axes.set_xticks(time_values)
    axes.set_xticklabels(timevaluemonths)
    axes.set_yticks(np.arange(0, max(time_data), 50000))
    axes.set_title('Number of Crimes by Month')
    axes.color_palette = colors
    
    # set the bar color using the line palette
    
    plt.Color = colors
    plt.show()
    
get_graph()