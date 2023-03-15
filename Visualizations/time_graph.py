import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import dataset as dataset

def get_graph():
    # Get the dataset
    crime_ds = dataset.get_dataset()

    # Get the time data
    times_raw = [i for i in crime_ds['CMPLNT_FR_TM'] if type(i) != float]

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
    time_values = np.arange(0, 24, 1)
    time_values_labels= ['12 AM', '1 AM', '2 AM', '3 AM', '4 AM', '5 AM', '6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM', '9 PM', '10 PM', '11 PM']
    # Plot the data
    axes.bar(time_values, time_data)

    # Configure the graph
    axes.set_xlabel('Time of Day')
    axes.set_ylabel('Number of Crimes')
    axes.set_xticks(time_values)
    axes.set_xticklabels(time_values_labels)
    axes.set_yticks(np.arange(0, max(time_data), 50000))
    axes.set_title('Number of Crimes by Time of Day')

    plt.show()


def get_line_graph():
    # Do the same thing as get_graph() but with a line graph
    # Get the dataset
    crime_ds = dataset.get_dataset()

    # Get the time data
    times_raw = [i for i in crime_ds['CMPLNT_FR_TM'] if type(i) != float]

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
    time_values = np.arange(0, 24, 1)

    # Plot the data
    axes.plot(time_values, time_data)
    time_values_labels= ['12 AM', '1 AM', '2 AM', '3 AM', '4 AM', '5 AM', '6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM', '9 PM', '10 PM', '11 PM']


    axes.set_xlabel('Time of Day')
    axes.set_ylabel('Number of Crimes')
    axes.set_xticks(time_values)
    axes.set_xticklabels(time_values_labels)
    axes.set_yticks(np.arange(0, max(time_data), 10000))
    axes.set_title('Number of Crimes by Time of Day')
    
    plt.show()

get_line_graph()
