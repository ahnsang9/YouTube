import pandas as pd
import numpy as np
from selenium import webdriver
import time
from pytube import YouTube

driver = webdriver.Chrome('C:\\Users\안상훈\PycharmProjects\chromedriver.exe') #크롬 드라이버 실행

data = pd.read_excel('melon_힙_list.xlsx')  # 플레이리스트 엑셀에서 데이터 불러오기
titles = data['title']
singers = data['singer']
albums = data['album']

urls = []
driver.get('https://www.youtube.com/')

for i in range(10):
    time.sleep(1)
    element = driver.find_element_by_name("search_query") #search창 지정
    element.clear() #search창 클리어
    #element.send_keys(f'{titles[i]} {singers[i]} {albums[i]}')
    element.send_keys(f'{titles[i]} {singers[i]} audio')
    driver.find_element_by_xpath('// *[ @ id = "search-icon-legacy"]').click()  # 검색버튼 클릭

    time.sleep(1)
    first = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/'
                                         'ytd-search/div[1]/ytd-two-column-search-'
                                         'results-renderer/div/ytd-section-list-renderer'
                                         '/div[2]/ytd-item-section-renderer/div[3]/ytd-video'
                                         '-renderer[1]/div[1]/div/div[1]/div/h3/a')
    driver.execute_script("arguments[0].click();", first)
    while(True):
            try:
                url = driver.current_url
                urls.append(driver.current_url) #현재 페이지 url 복사
                break
            except:pass

driver.close()
df = pd.DataFrame({'urls' : urls})
df.to_excel("urls.xlsx", encoding='utf-8')
