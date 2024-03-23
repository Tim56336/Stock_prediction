import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


pre_path = r'C:\Users\tim56\OneDrive\Documents\py\stock_prediction\Nonstationary_Transformers\results\Stock2330_ns_Transformer_custom_ftM_sl30_ll0_pl1_dm512_nh8_el2_dl1_df2048_fc3_ebtimeF_dtTrue_stock2330_0\pred.npy'
pred = np.load(pre_path)
gt_path = r'C:\Users\tim56\OneDrive\Documents\py\stock_prediction\Nonstationary_Transformers\results\Stock2330_ns_Transformer_custom_ftM_sl30_ll0_pl1_dm512_nh8_el2_dl1_df2048_fc3_ebtimeF_dtTrue_stock2330_0\true.npy'
ground_truth = np.load(gt_path)
metrics_path = r'C:\Users\tim56\OneDrive\Documents\py\stock_prediction\Nonstationary_Transformers\results\Stock2330_ns_Transformer_custom_ftM_sl30_ll0_pl1_dm512_nh8_el2_dl1_df2048_fc3_ebtimeF_dtTrue_stock2330_0\metrics.npy'
metrics = np.load(metrics_path)
# print(pred.shape)
# print(ground_truth.shape)

csv_path = r'C:\Users\tim56\OneDrive\Documents\py\stock_prediction\stock01.csv'
df = pd.read_csv(csv_path)
cols = 'date','capacity','turnover','change','transaction_volume'
for col in cols:    
    df.drop(col, axis=1, inplace=True)
data_np = df.to_numpy()
mean = np.mean(data_np, axis=0)
std = np.std(data_np, axis=0)

# print(mean.shape, std.shape)


for item in range(0,4):
    x = np.arange(383)
    plt.plot(x, ground_truth[:,:, item]*std[item]+mean[item], label="Ground Truth")
    plt.plot(x, pred[:,:, item]*std[item]+mean[item], label="Pred")
    if item ==0:
        plt.title('High')
    elif item ==1:
        plt.title('Low')
    elif item ==2:
        plt.title('Close')
    else :
        plt.title('Open')
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

# mae, mse, rmse, mape, mspe = metrics
# print(rmse)
# x = np.arange(383)
# plt.plot(x, rmse, label="Ground Truth")
# plt.xlabel("epoch")
# plt.ylabel("emse")
# plt.legend()

# 顯示圖表



