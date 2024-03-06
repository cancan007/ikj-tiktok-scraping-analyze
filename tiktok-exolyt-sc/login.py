from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome import service as fs
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

profile_path = '/Users/moueshouta/Library/Application Support/Google/Chrome/'
account_name = 'Default' #User Data/(xxx)に表示されている名前、メインアカウントは基本「Default」に保存されているはずです

#Googleにログインした状態でスクレイピングするための設定
options = Options()
options.add_argument('--user-data-dir=' + profile_path)
options.add_argument(f'--profile-directory={account_name}')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--no-sandbox")

USER=os.getenv('USER_EMAIL')
PASS=os.getenv('PASS')
chrome_service = fs.Service(executable_path='../chromedriver')
driver = webdriver.Chrome(service=chrome_service
                          ,options=options # Googleログイン状態にしたければコメント解除
                          )
driver.get('https://exolyt.com/auth/login?error=AccessDenied')

input_user=driver.find_elements(By.CLASS_NAME,'shadow-sm')[0]
input_user.send_keys(USER)
input_pass=driver.find_elements(By.CLASS_NAME,'shadow-sm')[1]
input_pass.send_keys(PASS)
time.sleep(1)
login_btn = driver.find_elements(By.CLASS_NAME,'exolyt-button')[0]
login_btn.click()
time.sleep(5)
