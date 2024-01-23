from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome import service as fs
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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
driver.get('https://www.tiktok.com/login/phone-or-email/email')

input_id = driver.find_element(By.CLASS_NAME,'tiktok-11to27l-InputContainer')
input_id.clear()
input_id.send_keys(USER)
input_pass=driver.find_element(By.CLASS_NAME,'tiktok-wv3bkt-InputContainer')
input_pass.clear()
input_pass.send_keys(PASS)
login_btn=driver.find_element(By.CLASS_NAME,'tiktok-11sviba-Button-StyledButton')
login_btn.click()
print('30秒の間に手動のログインプロセスを終わらしてログイン状態にしてください')
time.sleep(30)
