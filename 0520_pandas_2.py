import pandas as pd

# 準備好題目要求的資料
products = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Guava']
prices = [30, 20, 25, 60, 45, 35]
sales = [100, 150, 80, 60, 90, 54]

# --- 題目要求：請分別使用「字典」與「列表（子列表）」兩種方式建立 DataFrame ---

# 方式一：使用字典建立
data_dict = {
    'Product': products,
    'Price': prices,
    'Sales': sales
}
df_from_dict = pd.DataFrame(data_dict)

# 方式二：使用列表（子列表）建立
data_list = []
for i in range(len(products)):
    data_list.append([products[i], prices[i], sales[i]])
df_from_list = pd.DataFrame(data_list, columns=['Product', 'Price', 'Sales'])

# 接下來使用 df_from_dict 來做後續的輸出（兩者內容完全一樣）
df = df_from_dict

# 1. 觀察資料的前 5 筆與後 5 筆內容
# 注意：範例輸出直接列出 head 和 tail，中間沒有加額外中文字
print(df.head(5))
print(df.tail(5))

# 2. 回傳資料的列數與欄數
print(df.shape)

# 3. 回傳欄位名稱
print(df.columns)

# 4. 顯示資料型態 (這裡範例的 Product 是 str)
print(df.dtypes)

# 5. 顯示非空值數量
print(df.count())

# 6. 計算數值欄位的統計資訊（平均、標準差、最大值、最小值與四分位數，皆取小數後2位）
# 使用 .describe()，再用 .round(2) 限制小數點位數
summary_stats = df.describe().round(2)
print(summary_stats)

# 7. 把統計資訊存檔為 0520_stock2.csv
summary_stats.to_csv("0520_stock2.csv")