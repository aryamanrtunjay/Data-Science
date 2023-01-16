import matplotlib.pyplot as plt
import dataset

def get_graph():
    crime_dataset = dataset.get_dataset()
    premise_classes = []
    all_premise_classes = []

    for i in range(len(crime_dataset)):
        premise = crime_dataset['PREM_TYP_DESC'][i]
        if premise != 'UNKNOWN' and premise != "OTHER" and premise != "" and type(premise) == str:
            if premise not in premise_classes:
                premise_classes.append(premise)
                all_premise_classes.append(1)
            else:
                all_premise_classes[premise_classes.index(premise)] += 1

    cleaned_premise_descs = []
    cleaned_premise_descs_classes = []
    for i in all_premise_classes:
        if i / sum(all_premise_classes) > 2:
            cleaned_premise_descs.append(i)
            cleaned_premise_descs_classes.append(premise_classes[all_premise_classes.index(i)])
        else:
            if "OTHER" not in cleaned_premise_descs_classes:
                cleaned_premise_descs_classes.append("OTHER")
                cleaned_premise_descs.append(i)
            else:
                cleaned_premise_descs[cleaned_premise_descs_classes.index("OTHER")] += 1

    fig = plt.figure(0)
    axes = fig.add_subplot(111)
    axes.pie(all_premise_classes, labels=premise_classes, autopct='%1.1f%%')
    plt.show()

get_graph()