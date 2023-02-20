import matplotlib.pyplot as plt
import numpy as np
import dataset as dataset
import datetime as dt

def get_graph():
    crime_ds = dataset.get_dataset()
    times_raw = [i for i in crime_ds['CMPLNT_FR_DT'] if type(i) != float]
    all_times = []

    for i in range(len(times_raw)):
        all_times.append(dt.datetime.strptime(times_raw[i], '%m/%d/%Y'))
    # Get the day of the week for each datetime object
    days = [i.weekday() for i in all_times]
    # Get the number of crimes for each day of the week
    day_data = [0 for i in range(7)]
    for i in days:
        day_data[i] += 1
    # Set up the graph
    fig = plt.figure()
    axes = fig.add_subplot(111)
    # Set the x-axis labels
    day_values = np.arange(0, 7, 1)
    # Plot the data
    axes.bar(day_values, day_data)
    # Configure the graph
    axes.set_xlabel('Day of the Week')
    axes.set_ylabel('Number of Crimes')
    axes.set_xticks(day_values)
    axes.set_yticks(np.arange(0, max(day_data), 50000))
    axes.set_title('Number of Crimes by Day of the Week')
    plt.show()

get_graph()


