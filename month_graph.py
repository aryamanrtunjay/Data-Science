import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import dataset as dataset

def get_graph():
    # Get the dataset
    crime_ds = dataset.get_dataset()

    # Get the time data
    times_raw = [i for i in crime_ds['CMPLNT_FR_DT'] if type(i) != float]
    pdb.set_trace()
    # Get the hour of each time
    all_times = []
    for i in range(len(times_raw)):
        all_times.append(int(times_raw[i][0:2]))

    # Get the number of crimes for each hour
    time_data = [0 for i in range(24)]
    for i in all_times:
        time_data[i] += 1

    # Set up the graph
    fig = plt.figure()
    axes = fig.add_subplot(111)

    # Set the x-axis labels
    time_values = np.arange(1, 12, 1)

    # Plot the data
    axes.bar(time_values, time_data)

    # Configure the graph
    axes.set_xlabel('Time of Day')
    axes.set_ylabel('Number of Crimes')
    axes.set_xticks(time_values)
    axes.set_yticks(np.arange(0, max(time_data), 50000))
    axes.set_title('Number of Crimes by Month')

    plt.show()
    
get_graph()