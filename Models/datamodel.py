import tensorflow as tf
import keras
from keras import backend as K
from keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from tensorflow.python.keras import *
import numpy as np
from keras.layers import LeakyReLU, PReLU
import os
import pdb
import wandb

print("Num GPUs Avaialble: ", len(tf.config.experimental.list_physical_devices('GPU')))

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

if(os.path.exists(X_total_pickle) and os.path.exists(Y_total_pickle)):
    X_total = pd.read_pickle(X_total_pickle)
    Y_total = pd.read_pickle(Y_total_pickle)
else:
    if os.path.exists('../data.pickle'):
        dataset = pd.read_pickle('./data.pickle')
    else:
        dataset = pd.read_csv("./NYPD_Complaint_Data_Historic.csv", low_memory=False)
        dataset.to_pickle('./data.pickle')
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
    pd.to_pickle(X_total, "../X_total.pickle")
    pd.to_pickle(Y_total, "../Y_total.pickle")



X_train, X_test, Y_train, Y_test = train_test_split(X_total, Y_total, test_size= .1, random_state=2025)

# wandb.init(project="nypd-crime", name="NYPD-Crime-ANN")
model = keras.Sequential([
    keras.layers.Dense(256, activation='relu', input_shape = (3, )), # input layer
    keras.layers.Dense(32, activation='relu'), # hidden layer
    keras.layers.Dense(64, activation='relu'),  # hidden layer
    keras.layers.Dense(128, activation='relu'), # hidden layer
    keras.layers.Dense(128, activation='relu'), # hidden layer
    keras.layers.Dense(64, activation='relu'), # hidden layer
    keras.layers.Dense(32, activation='relu'), # hidden layer
    keras.layers.Dense(256, activation='softmax') # output layer
])

model.compile(optimizer='adam',
              loss='SparseCategoricalCrossentropy',
              metrics=['Accuracy'])
K.set_value(model.optimizer.learning_rate, 0.001)

model.fit(X_train, Y_train, epochs=200, batch_size=10)
model.evaluate(X_test, Y_test)


