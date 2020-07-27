import requests
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')  # headless 옵션 설정
options.add_argument("no-sandbox")  # headless 옵션 설정
options.add_argument('window-size=1920x1080')  # 브라우저 윈도우 사이즈
options.add_argument("disable-gpu")  # 사람처럼 보이게 하는 옵션들 # 가속 사용 x
options.add_argument("lang=ko_KR")  # 사람처럼 보이게 하는 옵션들 # 가짜 플러그인 탑재

#driver_path = 'C:\\Users\82105\PycharmProjects\YouTube_git2\chromedriver.exe'
driver_path = 'C:\\Users\안상훈\PycharmProjects\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=options)
driver.get('https://www.melon.com/song/detail.htm?songId=106215')

lyrics_temp = driver.find_element_by_class_name('lyric')
print(lyrics_temp.text)
driver.quit()




