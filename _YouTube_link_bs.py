import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import time
import re
import random

MAX_SLEEP_TIME = 3


data = pd.read_excel('melon_힙_list.xlsx')  # 플레이리스트 엑셀에서 데이터 불러오기

titles = data['title']
singers = data['singer']
albums = data['album']

urls = []

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}


for i in range(1):

    rand_value = random.randint(1, MAX_SLEEP_TIME)
    time.sleep(rand_value)

    KEY = str(str(f'{titles[i]} {singers[i]} audio'.encode('utf8'))).replace("\\x", "%").replace("b'", "")
    URL = 'https://www.melon.com/index.htm'
    pattern = re.compile(r'\s+')
    URL = re.sub(pattern, '', URL)

    session = requests.Session()
    html = session.get(URL, headers = headers).text
    bsObj = bs(html,'html.parser')

    link = bsObj.select('#gnb_menu > ul.sub_gnb > li:nth-child(1) > a')
print(link)