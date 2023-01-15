import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import dataset as dataset
import dataset

def get_graph():
    crime_ds = dataset.get_dataset()
    crime_desc_classes = []
    all_crime_descs = []

    for i in range(len(crime_ds)):
        crime_type = crime_ds['LAW_CAT_CD'][i]
        if crime_type == 'FELONY':
            crime_desc = crime_ds['OFNS_DESC'][i]
            if(crime_desc not in crime_desc_classes):
                crime_desc_classes.append(crime_desc)
                all_crime_descs.append(1)
            else:
                all_crime_descs[crime_desc_classes.index(crime_desc)] += 1

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

    fig = plt.figure()
    pdb.set_trace()
    axes = fig.add_subplot(111)
    axes.pie(cleaned_crime_descs, labels=cleaned_crime_desc_classes, autopct='%1.1f%%')
    plt.show()