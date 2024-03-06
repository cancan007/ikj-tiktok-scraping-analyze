from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome import service as fs
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import numpy as np
import datetime
import os

profile_path = '/Users/moueshouta/Library/Application Support/Google/Chrome/'
account_name = 'Default' #User Data/(xxx)に表示されている名前、メインアカウントは基本「Default」に保存されているはずです

#Googleにログインした状態でスクレイピングするための設定
options = Options()
options.add_argument('--user-data-dir=' + profile_path)
options.add_argument(f'--profile-directory={account_name}')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--no-sandbox")


chrome_service = fs.Service(executable_path='../chromedriver')
driver = webdriver.Chrome(service=chrome_service
                          ,options=options # Googleログイン状態にしたければコメント解除
                          )

hashtags = input("流行を調べたいハッシュタグを複数記入してください(間は半角空白で区切る)").split()
#hashtags = ["就活","大学生","高校生","学部","24卒","25卒","26卒","仕事","悩み","相談",'ikj共感コミュニティー','インカレ','学生','ソフトボール','ベンチャー','業界','就活生','自己分析','必見','面接対策','言葉遣い','ダンス','就活あるある','学生団体','軸','就活軸']
infos=[]
for t in hashtags: 
    driver.get(f"https://exolyt.com/hashtags/{t}#t-overview")
    time.sleep(4)
    parent = driver.find_elements(By.CLASS_NAME,'jsx-882128346')[0]
    p2s = parent.find_elements(By.CLASS_NAME,'totalbox')
    p2s.pop(4)
    p2s.pop(3)
    info = [t] + list(map(lambda x: x.find_element(By.CLASS_NAME,'font-bold').text, p2s))
    infos.append(info)
    print(info)
    print("###########")
    

df=pd.DataFrame(np.array(infos),
                  columns=['Tag', 'Total_views', 'Videos', 'Avg_Views/Video'])

dt_now = datetime.datetime.now()
dt_today=f"{dt_now.year}-{dt_now.month}-{dt_now.day}"
#os.makedirs(f'./data/{dt_today}/', exist_ok=True)
df.to_csv(f'./data/{dt_today}-tiktok-tag-data.csv')
print('終了')


