from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_recall_fscore_support
import pandas as pd
import torch
from torch import nn
import numpy as np
import os
import pdb
import wandb


input_dim = 3

hidden_layers = 26

output_dim = 8
class NeuralNetwork(nn.Module):
  def __init__(self):
    super(NeuralNetwork, self).__init__()
    self.linear1 = nn.Linear(input_dim, hidden_layers)
    self.GELU1 = nn.GELU
    self.linear2 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU2 = nn.GELU
    self.linear3 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU3 = nn.GELU
    self.linear4 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU4 = nn.GELU
    self.linear5 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU5 = nn.GELU
    self.linear6 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU6 = nn.GELU
    self.linear7 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU7 = nn.GELU
    self.linear8 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU8 = nn.GELU
    self.linear9 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU9 = nn.GELU
    self.linear10 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU10 = nn.GELU
    self.linear11 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU11 = nn.GELU
    self.linear12 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU12 = nn.GELU
    self.linear13 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU13 = nn.GELU
    self.linear14 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU14 = nn.GELU
    self.linear15 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU15 = nn.GELU
    self.linear16 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU16 = nn.GELU
    self.linear17 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU17 = nn.GELU
    self.linear18 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU18 = nn.GELU
    self.linear19 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU19 = nn.GELU
    self.linear20 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU20 = nn.GELU
    self.linear21 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU21 = nn.GELU
    self.linear22 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU22 = nn.GELU
    self.linear23 = nn.Linear(hidden_layers, hidden_layers)
    self.GELU23 = nn.GELU
    self.linear24 = nn.Linear(hidden_layers, output_dim)

  def forward(self, x):
    x = torch.softmax(self.linear1(x), dim=1)
    x = self.linear2(x)
    return x

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

X_train = torch.tensor(X_train.values)
Y_train = torch.tensor(Y_train.values)
X_test = torch.tensor(X_test.values)
Y_test = torch.tensor(Y_test.values)

train_end = int(len(X_train)*0.05)
test_end = int(len(X_test)*0.05)

X_train = X_train[:train_end]
Y_train = Y_train[:train_end]
X_test = X_test[:test_end]
Y_test = Y_test[:test_end]

# Calculate the number of unique classes in Y_train

# wandb.init(project="nypd-crime", name="NYPD-Crime-ANN")

model = NeuralNetwork().cuda()

num_epochs = 100
batch_size = 128
cost_function = nn.CrossEntropyLoss()
gradient_descent = torch.optim.Adam(model.parameters(),
                                lr=0.001,
                                weight_decay=1e-3,)

losses = []
for epoch in range(num_epochs):
    fscore = []
    cost = 0
    print(epoch)
    for i in range(0, len(X_train), batch_size):
        batch = X_train[i:i+batch_size].cuda()
        target = Y_train[i:i+batch_size].cuda()
        batch = batch.to(torch.float32)

        target_list = [target[i] for i in range(len(target))]
        target = torch.tensor(target_list)
        target = target.type(torch.LongTensor)
        target = target.cuda()

        out = model(batch)
        cost = cost_function(out, target)
        losses.append(cost.item())
        cost.backward()
        gradient_descent.step()

        softmax_function = torch.nn.Softmax(dim=1)
        precision, recall, fscore, support = precision_recall_fscore_support(target.cpu(), torch.argmax(softmax_function(out.data), dim=1).cpu(),
                                                                        zero_division=0, labels=(0,1,2,3,4,5,6,7))
        
    print("Epoch: ", epoch, "Cost", '{0:.3g}'.format(cost.item()), "F1-Score: ", '{0:.3g}'.format(sum(fscore)/len(fscore)), end="")

