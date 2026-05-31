import os
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_dir, "SuperMarket Analysis.csv")
output_file = os.path.join(current_dir, "0520_pandas_3OK.CSV")

if not os.path.exists(input_file):
    print(f"❌ 錯誤：找不到檔案 {input_file}")
else:
    # 1. 讀取與篩選資料
    df = pd.read_csv(input_file)
    
    # 印出檔案內實際的所有欄位名稱，確認到底叫什麼
    print("📊 檔案裡的實際欄位有：", df.columns.tolist())
    print("-" * 50)
    
    filtered_df = df[df['Branch'].str.startswith('A') & (df['Customer type'] == 'Member')]

    # ==========================================
    # ==========================================
    
    # 2. 計算產品線的 Sales 與 Rating
    sales_sum = filtered_df.groupby('Product line')['Sales'].sum()
    rating_mean = filtered_df.groupby('Product line')['Rating'].mean()
    
    # 把算好的兩個結果合併成一個新的表格
    product_analysis = pd.DataFrame({
        'Sales': sales_sum,
        'Rating': rating_mean
    }).round(2)
    
    print("--- 產品線計算結果 ---")
    print(product_analysis)
    print("-" * 30)

    # 3. 計算 City 與 Gender 的平均銷售與筆數
    avg_sales = filtered_df.groupby(['City', 'Gender'])['Sales'].mean()
    count_sales = filtered_df.groupby(['City', 'Gender'])['Sales'].count()
    
    city_gender_analysis = pd.DataFrame({
        'Average_Sales': avg_sales,
        'Transaction_Count': count_sales
    }).round(2)

    # 4. 找出總銷售額最高的產品線
    top_product = product_analysis['Sales'].idxmax()
    max_sales = product_analysis['Sales'].max()
    print(f"★ 總銷售額最高的產品線為: {top_product} ({max_sales})")
    print("-" * 30)

    # 5. 強制輸出 CSV 檔案
    product_analysis.to_csv(output_file, encoding='utf-8-sig')
    
    print(f"\n✅ 終於成功啦！CSV 檔案已經乖乖躺在這裡了：\n👉 {output_file}")