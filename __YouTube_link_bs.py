import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import time
from urllib.request import urlopen
from pytube import YouTube
import re
import random

MAX_SLEEP_TIME = 3


data = pd.read_excel('melon_힙_list.xlsx')  # 플레이리스트 엑셀에서 데이터 불러오기

titles = data['title']
singers = data['singer']
albums = data['album']

urls = []

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}


for i in range(3):

    rand_value = random.randint(1, MAX_SLEEP_TIME)
    time.sleep(rand_value)

    KEY = str(str(f'{titles[i]} {singers[i]} audio'.encode('utf8'))).replace("\\x", "%").replace("b'", "")
    URL = "https://www.youtube.com/results?search_query=" + KEY
    pattern = re.compile(r'\s+')
    URL = re.sub(pattern, '', URL)

    session = requests.Session()
    html = session.get(URL, headers = headers).text
    bsObj = bs(html,'html.parser')

    link = bsObj.select('a')
    #Link = "https://www.youtube.com" + link.find("href").replace("..", "").replace("./", "", 1)
    #soup = bs(urlopen(URL), "html.parser", from_encoding='utf-8')
    #parselink = soup.find_all('div')
    #print(parselink)
    # Link = "https://www.youtube.com" + parselink.get("href").replace("..", "").replace("./", "", 1)


    '''while(True):
        try:
            a_tag = bs(requests.get(url).content, "html.parser").find("a",{'class':"yt-simple-endpoint style-scope ytd-video-renderer"})
            print(a_tag["href"])
            break
        except:pass'''
