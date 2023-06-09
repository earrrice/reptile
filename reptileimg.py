import requests
from bs4 import BeautifulSoup
import os


url = 'https:'  # 要爬取的網站URL
save_directory = 'img'  # 圖片儲存目錄

def download_images(url, save_dir):
    # 發送GET請求
    response = requests.get(url)
    
    # 解析HTML內容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 找到所有圖片標籤
    img_tags = soup.find_all('img')
    
    # 迭代處理每個圖片標籤
    for img in img_tags:
        # 取得圖片的URL
        img_url = img['src']
        
        # 檢查圖片URL是否為絕對路徑
        if not img_url.startswith('http'):
            img_url = url + img_url
        
        try:
            if img_url.lower().endswith('.jpg'):# 檢查圖片檔案擴展名是否為 .jpg 如果只要下載特定檔案的話
                # 發送GET請求下載圖片
                response = requests.get(img_url)
            
                # 確認請求成功
                response.raise_for_status()
            
                # 提取圖片檔名
                img_name = img_url.split('/')[-1]
            
                # 組合圖片的儲存路徑
                save_path = os.path.join(save_dir, img_name)
            
                # 儲存圖片到本地
                with open(save_path, 'wb') as f:
                    f.write(response.content)
            
                print(f"已下載圖片: {img_name}")
            else:
                print(f"非 JPEG 圖片: {img_url}")
        
        except Exception as e:
            print(f"下載失敗: {img_url}")
            print(f"錯誤訊息: {str(e)}")



# 建立圖片儲存目錄（如果不存在）
os.makedirs(save_directory, exist_ok=True)

# 呼叫函式開始爬取圖片
download_images(url, save_directory)
