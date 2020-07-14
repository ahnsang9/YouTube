import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
from pytube import YouTube
import re

#driver = webdriver.Chrome('C:\\Users\안상훈\PycharmProjects\chromedriver.exe') #크롬 드라이버 실행

data = pd.read_excel('melon_힙_list.xlsx') #플레이리스트 엑셀에서 데이터 불러오기
titles = data['title']
singers = data['singer']
albums = data['album']

urls = []
#driver.get('https://www.youtube.com/')

for i in range(10):
    #time.sleep(1)
    #element = driver.find_element_by_name("search_query") #search창 지정
    #element.clear() #search창 클리어
    #element.send_keys(f'{titles[i]} {singers[i]} {albums[i]}')
    #element.send_keys(f'{titles[i]} {singers[i]} audio')
    KEY = str(f'{titles[i]} {singers[i]} audio'.encode('utf8')).replace("\\x", "%").replace("b'", "")
    URL = str("https://www.youtube.com/results?search_query=" + KEY)
    URL.replace(" ", "")
    pattern = re.compile(r'\s+')
    URL = re.sub(pattern, '', URL)
    #driver.get(URL)
    print(URL)
    time.sleep(3)
    #driver.find_element_by_xpath('// *[ @ id = "search-icon-legacy"]').click() #돋보기버튼 클릭
    '''while(True):
        try:
            #driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string').click()
            #driver.find_element_by_xpath('//*[@id="video-title"]').click() #첫번째 영상 클릭
            #hrefs = driver.find_element_by_xpath('//*[@id="video-title"]').get_attribute('href')
            url = driver.current_url
            a_tag = bs(requests.get(url).content, "html.parser").find("a",{'class':"yt-simple-endpoint style-scope ytd-video-renderer"})
            print(a_tag["href"])
            break
        except:pass'''


    #time.sleep(1)

'''while(True):
        try:
            urls.append(driver.current_url) #현재 페이지 url 복사
            break
        except:pass'''

print(urls)
driver.close()

'''for i in urls:
    yt = YouTube(i)
    yt_streams = yt.streams'''

