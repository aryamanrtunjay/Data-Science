import matplotlib.pyplot as plt
import numpy as np
import dataset as dataset
import datetime as dt 

def get_graph(year: int):
    crime_ds = dataset.get_dataset() 
    times_raw = [i for i in crime_ds['CMPLNT_FR_DT'] if type(i) != float]
    all_times = []

    for i in range(len(times_raw)):
        all_times.append(dt.datetime.strptime(times_raw[i], '%m/%d/%Y'))
    
    # Get the year for each datetime object
    years = [i.year for i in all_times]
    # Get the number of crimes in each month for each year
    month_data = [0 for i in range(12)]
    for i in range(len(years)):
        if years[i] == year:
            month_data[all_times[i].month - 1] += 1
    
    # Set up the graph
    fig = plt.figure()
    axes = fig.add_subplot(111)
    # Set the x-axis labels
    month_values = np.arange(0, 12, 1)
    # Plot the data
    axes.bar(month_values, month_data)
    # Configure the graph
    month_value_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    axes.set_xlabel('Month in ' + str(year))
    axes.set_ylabel('Number of Crimes')
    axes.set_xticks(month_values)
    axes.set_xticklabels(month_value_labels)
    axes.set_yticks(np.arange(0, max(month_data), 50000))
    axes.set_title('Crimes vs Month in ' + str(year))
    plt.show()

get_graph(2023)
