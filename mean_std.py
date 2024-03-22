import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
path = r'C:\Users\tim56\OneDrive\Documents\py\stock_prediction\Nonstationary_Transformers\data\stock\pred.csv'
df_raw = pd.read_csv(path)
      
cols = list(df_raw.columns)
cols.remove('date')
cols.remove('capacity')
cols.remove('turnover')
cols.remove('change')
cols.remove('transaction_volume')
df_raw = df_raw[cols]
data_np = df_raw.to_numpy()
mean = np.mean(data_np, axis=0)
std = np.std(data_np, axis=0)
print(mean, std)
