import os
import cv2
from deepface import DeepFace

# 1. 設定資料夾路徑
input_dir = 'face_data'      
output_dir = 'face_data_ok'  

# 如果輸出資料夾不存在，就建立一個
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 確保輸入資料夾存在
if not os.path.exists(input_dir):
    print(f"❌ 錯誤：找不到 '{input_dir}' 資料夾！")
    print(f"請先建立 {input_dir} 資料夾，並把 Sad, Angry, Happy 的圖片放進去。")
else:
    print(f"開始處理 '{input_dir}' 中的圖片...\n")
    
    # 2. 走訪 face_data 裡面的所有圖片
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            # 篩選圖片副檔名
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(root, file)
                print(f"正在分析: {file} ...")

                try:
                    # 3. 使用 DeepFace 分析情緒
                    # enforce_detection=False 代表就算沒抓到清楚的臉也不會讓程式當掉
                    results = DeepFace.analyze(img_path, actions=['emotion'], enforce_detection=False)

                    # DeepFace 若辨識到多張臉會回傳 List，取第一張臉
                    if isinstance(results, list):
                        result = results[0]
                    else:
                        result = results

                    # 取得主要情緒與臉部位置座標
                    dominant_emotion = result['dominant_emotion']
                    region = result['region']
                    x, y, w, h = region['x'], region['y'], region['w'], region['h']

                    # 4. 用 OpenCV 讀取圖片，畫上辨識框與文字
                    img = cv2.imread(img_path)
                    
                    # 畫綠色方框 (B, G, R)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    
                    # 寫上情緒文字
                    cv2.putText(img, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                    # 5. 儲存到 face_data_ok 資料夾
                    # 避免不同資料夾有同名圖片，這裡把原本的資料夾名稱加到檔名前面
                    parent_folder = os.path.basename(root)
                    if parent_folder != input_dir:
                        new_file_name = f"{parent_folder}_{file}"
                    else:
                        new_file_name = file
                        
                    output_path = os.path.join(output_dir, new_file_name)
                    cv2.imwrite(output_path, img)
                    
                    print(f"✅ 成功！已存至 {output_path}")

                except Exception as e:
                    print(f"⚠️ 處理 {file} 時發生錯誤略過: {e}")

    print("\n🎉 辨識任務全部結束！請查看 face_data_ok 資料夾看成果。")