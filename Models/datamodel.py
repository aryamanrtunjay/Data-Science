import tensorflow as tf
import keras
from keras import backend as K
from keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import os
import pdb
import wandb

# Read the dataset from a pickle file if it exists, else read from the csv file and create the pickle file

# Raghav Paths
# datapath = "/home/raghavkalyan/Files/Documents/Devolopment/TSA/Data-Science/NYPD_Complaint_Data_Historic.csv"
# X_total_pickle = "./X_total.pickle"
# Y_total_pickle = "./Y_total.pickle"
# data_pickle = "./data.pickle"

# Aryaman Paths
datapath = "../../NYPD_Complaint_Data_Historic.csv"
X_total_pickle = "../../X_total.pickle"
Y_total_pickle = "../../Y_total.pickle"
data_pickle = "../../data.pickle"

if(os.path.exists(X_total_pickle) and os.path.exist(Y_total_pickle)):
    X_total = pd.read_pickle(X_total_pickle)
    Y_total = pd.read_pickle(Y_total_pickle)
else:
    if os.path.exists(data_pickle):
        dataset = pd.read_pickle(data_pickle)
    else:
        dataset = pd.read_csv(datapath, low_memory=False)
        dataset.to_pickle(data_pickle)
    # Get train and test datasets
    subset = dataset[['CMPLNT_FR_TM','ADDR_PCT_CD', 'LAW_CAT_CD', 'SUSP_RACE']].copy(deep=True)
    subset.dropna(axis = 0, inplace=True)

    X_total = subset[['CMPLNT_FR_TM', 'ADDR_PCT_CD', 'LAW_CAT_CD']].copy(deep=True)
    Y_total = subset['SUSP_RACE'].copy(deep=True)

    unique1 = X_total['LAW_CAT_CD'].unique().tolist()
    unique2 = X_total['ADDR_PCT_CD'].unique().tolist()

    for i in range(len(unique1)):
        idx = unique1.index(unique1[i])
        idx2 = unique2.index(unique2[i])
        X_total['LAW_CAT_CD'].replace(unique1[i], idx, inplace=True)
        X_total['ADDR_PCT_CD'].replace(unique2[i], idx2, inplace=True)
        
    le = LabelEncoder()
    Y_total = le.fit_transform(Y_total)
    Y_total = pd.DataFrame(Y_total)
    
    X_total['CMPLNT_FR_TM'] = X_total['CMPLNT_FR_TM'].str.split(':').str[0]
    X_total['CMPLNT_FR_TM'] = X_total['CMPLNT_FR_TM'].astype(int)
    pd.to_pickle(X_total, X_total_pickle)
    pd.to_pickle(Y_total, Y_total_pickle)

X_train, X_test, Y_train, Y_test = train_test_split(X_total, Y_total, test_size=0.2, random_state=2023)

# wandb.init(project="nypd-crime", name="NYPD-Crime-ANN")
model = keras.Sequential([
    keras.layers.Dense(32, input_shape=(3,), activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(32, activation='softmax')
])

model.compile(optimizer='AdaGrad',
              loss='sparse_categorical_crossentropy',
              metrics=['Accuracy'])
K.set_value(model.optimizer.learning_rate, 0.1)

model.fit(X_train, Y_train, epochs=400, batch_size=100)
model.evaluate(X_test, Y_test)