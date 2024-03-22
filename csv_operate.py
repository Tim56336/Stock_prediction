import csv

# 讀入 CSV 檔案
path = r'C:\Users\tim56\OneDrive\Documents\py\stock_prediction\Nonstationary_Transformers\data\stock\2330_0322.csv'
with open(path, "r") as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# 取出連續 30 筆資料
start_index = 18
end_index = start_index + 30

continuous_data = data[start_index:end_index]

# 輸出結果
with open("output_30.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(data[0])
    writer.writerows(continuous_data)
