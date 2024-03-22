import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

path = r'C:\Users\tim56\OneDrive\Documents\py\stock_prediction\Nonstationary_Transformers\data\stock\output_30.csv'
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
# print(mean, std)


pre_path = r'C:\Users\tim56\OneDrive\Documents\py\stock_prediction\Nonstationary_Transformers\results\Stock2330_ns_Transformer_custom_ftM_sl30_ll0_pl1_dm512_nh8_el2_dl1_df2048_fc3_ebtimeF_dtTrue_stock2330_0\real_prediction.npy'
pred = np.load(pre_path)
pred = pred * std + mean
print(pred)