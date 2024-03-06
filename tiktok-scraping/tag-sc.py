from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome import service as fs
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import numpy as np

profile_path = '/Users/moueshouta/Library/Application Support/Google/Chrome/'
account_name = 'Default' #User Data/(xxx)に表示されている名前、メインアカウントは基本「Default」に保存されているはずです

#Googleにログインした状態でスクレイピングするための設定
options = Options()
options.add_argument('--user-data-dir=' + profile_path)
options.add_argument(f'--profile-directory={account_name}')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--no-sandbox")


USER='ikj.outdoor.feat.ah@gmail.com'
PASS='kuruwa21'
chrome_service = fs.Service(executable_path='../chromedriver')
driver = webdriver.Chrome(service=chrome_service
                          ,options=options # Googleログイン状態にしたければコメント解除
                          )


# Googleの検索TOP画面を開く

tag_name = input("スクレイピングしたいタグ名を入力してください")
driver.get(f"https://www.tiktok.com/tag/{tag_name}?lang=ja-JP")

time.sleep(10)
rows=driver.find_elements(By.CLASS_NAME,'tt-live-table-row')
infos=[]
for r in rows:
    tds= r.find_elements(By.TAG_NAME, 'td')
    tds.pop(6)
    info=list(map(lambda x: x.text, tds))
    infos.append(info)
    print(info)
    print("###########")
    
next_btn=driver.find_element(By.CLASS_NAME,'tt-live-pagination-next-page')
isEnable=next_btn.is_enabled()
while isEnable:
    current_next_btn=driver.find_element(By.CLASS_NAME,'tt-live-pagination-next-page')
    rows=driver.find_elements(By.CLASS_NAME,'tt-live-table-row')
    for r in rows:
        tds= r.find_elements(By.TAG_NAME, 'td')
        tds.pop(6)
        info=list(map(lambda x: x.text, tds))
        infos.append(info)
        print(info)
    print("###########")
    current_next_btn.click()
    time.sleep(1)
    next_btn=driver.find_element(By.CLASS_NAME,'tt-live-pagination-next-page')
    isEnable=next_btn.is_enabled()
df=pd.DataFrame(np.array(infos),
                  columns=['title', 'start_date_time', 'total_viewers','plus_followers', 'reward','time'])
df.to_csv('./data/tiktok-live-data.csv')
print('終了')


