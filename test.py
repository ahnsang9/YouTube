import requests
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
#options.add_argument('headless')  # headless 옵션 설정
#options.add_argument("no-sandbox")  # headless 옵션 설정
options.add_argument('window-size=1920x1080')  # 브라우저 윈도우 사이즈
options.add_argument("disable-gpu")  # 사람처럼 보이게 하는 옵션들 # 가속 사용 x
options.add_argument("lang=ko_KR")  # 사람처럼 보이게 하는 옵션들 # 가짜 플러그인 탑재

driver_path = 'C:\\Users\82105\PycharmProjects\YouTube_git2\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=options)
driver.get('https://www.youtube.com/results?search_query=%EB%8B%A4%EC%A7%90+%EC%A1%B0%EC%84%B1%EB%AA%A8+official+audio+mp3')
yt_url_back = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/'
                                                        'ytd-two-column-search-results-renderer/div/ytd-section-list-'
                                                        'renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-r'
                                                        'enderer[1]/div[1]/ytd-thumbnail/a').get_attribute('href')

driver.quit()
print(yt_url_back)