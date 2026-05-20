import pandas as pd

# 1. 先用 list 建立原始資料，並用 pd.Series 轉成 stock1
data_list = [120, 80, None, 60, 95, None, 110]
stock1 = pd.Series(data_list)
print("stock1")
print(stock1)
print("-" * 30)  # 分隔線，方便對照輸出

# 2. 加入指定水果索引建立 stock2
fruits = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Peach', 'Melon']
stock2 = pd.Series(data_list, index=fruits)
print("stock2")
print(stock2)
print("-" * 30)

# 3. 將 stock2 轉為字典 stock3
stock3 = stock2.to_dict()
print("stock3")
print(stock3)
print("-" * 30)

# 4. 輸出 Banana 的庫存值
# 注意：為了完全對齊範例的格式「Banana 庫存：80.0」，這裡使用 f-string 格式化輸出
print(f"Banana 庫存：{stock2['Banana']}")
print("-" * 30)

# 5. 計算與檢查缺失值
print("缺失值檢查：")
missing_check = stock2.isna()  # 或者用 .isnull()
print(missing_check)

missing_count = stock2.isna().sum()
print(f"缺失值數量：{missing_count}")
print("-" * 30)

# 6. 把 stock2 存檔為 0520_stock.csv
# 題目要求存成 csv，通常會保留 index（水果名稱），並給欄位一個名稱（例如 'Stock'）
stock2.to_csv("0520_stock.csv", header=["Stock"])
print("已成功將 stock2 存檔為 0520_stock.csv")