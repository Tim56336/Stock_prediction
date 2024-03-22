import matplotlib.pyplot as plt
import numpy as np

pre_path = r'C:\Users\tim56\OneDrive\Documents\py\stock_prediction\Nonstationary_Transformers\results\Stock2330_ns_Transformer_custom_ftM_sl30_ll0_pl1_dm512_nh8_el2_dl1_df2048_fc3_ebtimeF_dtTrue_stock2330_0\pred.npy'
pred = np.load(pre_path)
gt_path = r'C:\Users\tim56\OneDrive\Documents\py\stock_prediction\Nonstationary_Transformers\results\Stock2330_ns_Transformer_custom_ftM_sl30_ll0_pl1_dm512_nh8_el2_dl1_df2048_fc3_ebtimeF_dtTrue_stock2330_0\true.npy'
ground_truth = np.load(gt_path)
metrics_path = r'C:\Users\tim56\OneDrive\Documents\py\stock_prediction\Nonstationary_Transformers\results\Stock2330_ns_Transformer_custom_ftM_sl30_ll0_pl1_dm512_nh8_el2_dl1_df2048_fc3_ebtimeF_dtTrue_stock2330_0\metrics.npy'
metrics = np.load(metrics_path)
print(pred.shape)
print(ground_truth.shape)

# x = np.arange(383)
# plt.plot(x, ground_truth[:,:, 2], label="Ground Truth")
# plt.plot(x, pred[:,:, 2], label="Pred")
# plt.xlabel("Time")
# plt.ylabel("Price")
# plt.legend()

# mae, mse, rmse, mape, mspe = metrics
# print(rmse)
# x = np.arange(383)
# plt.plot(x, rmse, label="Ground Truth")
# plt.xlabel("epoch")
# plt.ylabel("emse")
# plt.legend()

# 顯示圖表
plt.show()


