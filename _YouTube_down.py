import pandas as pd
from selenium import webdriver
import time
from pytube import YouTube

driver = webdriver.Chrome('C:\\Users\안상훈\PycharmProjects\chromedriver.exe')

data = pd.read_excel('melon_힙_list.xlsx')
titles = data['title']
singers = data['singer']
albums = data['album']

urls = []
driver.get('https://www.youtube.com/')

for i in range(10):

    #time.sleep(1)
    element = driver.find_element_by_name("search_query")
    element.clear()
    element.send_keys(f'{titles[i]} {singers[i]} {albums[i]}')
    time.sleep(1)
    driver.find_element_by_xpath('// *[ @ id = "search-icon-legacy"]').click()
    time.sleep(1)
    while(True):
        try:
            driver.find_element_by_xpath('//*[@id="video-title"]').click()
            driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string').click()
            break
        except:pass
    time.sleep(1)
    while(True):
        try:
            urls.append(driver.current_url)
            break
        except:pass

print(urls)
driver.close()

'''for i in urls:
    yt = YouTube(i)
    yt_streams = yt.streams'''

