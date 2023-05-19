import matplotlib.pyplot as plt
import dataset
import seaborn as sns

def get_graph():
    crime_dataset = dataset.get_dataset()
    premise_classes = []
    all_premise_classes = []

    for i in range(len(crime_dataset)):
        premise = crime_dataset['PREM_TYP_DESC'][i]
        if premise != 'UNKNOWN' and premise != "OTHER" and premise != "" and premise != 'TRANSIT - NYC SUBWAY' and type(premise) == str:
            if premise not in premise_classes:
                premise_classes.append(premise)
                all_premise_classes.append(1)
            else:
                all_premise_classes[premise_classes.index(premise)] += 1

    cleaned_premise_descs = []
    cleaned_premise_descs_classes = []
    for i in all_premise_classes:
        if i / sum(all_premise_classes) > 0.019:
            cleaned_premise_descs.append(i)
            cleaned_premise_descs_classes.append(premise_classes[all_premise_classes.index(i)])

    plt.rcParams.update({'font.size': 23})
    plt.rc('axes', titlesize = 25) 
    plt.rc('axes', labelsize = 25)
    plt.rc('xtick', labelsize = 25) 
    plt.rc('ytick', labelsize = 25)
    plt.rc('legend', fontsize = 25)
    plt.rc('font', size = 27)
    color_palette = ['#f44336', '#6fa8dc', '#ffd966', '#b6d7a8']
    colors = sns.set_palette(sns.color_palette(color_palette)) 
    fig = plt.figure(0)
    axes = fig.add_subplot(111)
    axes.pie(cleaned_premise_descs, labels=cleaned_premise_descs_classes, autopct='%1.1f%%', colors= colors, radius = 1.4)
    plt.show()

get_graph()