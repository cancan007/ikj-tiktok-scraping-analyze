from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome import service as fs

chrome_service = fs.Service(executable_path='../chromedriver')
driver = webdriver.Chrome(service=chrome_service)

driver.get("https://livecenter.tiktok.com/analytics/live_video?lang=ja-JP")
driver.implicitly_wait(100)