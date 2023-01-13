import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import dataset as dataset
import dataset

crime_ds = dataset.get_dataset()
crimes = set(i for i in crime_ds['OFNS_DESC'] if type(i) != float)

pdb.set_trace()