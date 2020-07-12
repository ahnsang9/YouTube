import requests
from pandas import Series, DataFrame
import pandas
from bs4 import BeautifulSoup
pandas.set_option('display.max_columns',10)
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
for i in range(1):
    a = i * 50 + 1
    url = "https://www.melon.com/genre/song_list.htm?gnrCode=GN0300"
    #url = "https://www.melon.com/genre/song_listPaging.htm?startIndex=1&pageSize=51&gnrCode=GN0300&dtlGnrCode=&orderBy=NEW&steadyYn=N"
    result = requests.get(url, headers = header)
    obj = BeautifulSoup(result.text, "html.parser")

    titles = obj.select("div.wrap_song_info div.rank01 span a" )
    singers = obj.select("div.wrap_song_info div.rank02 span" )

    title = []
    singer = []

    for i in titles:
        title.append(i.text)
    for i in singers:
        singer.append(i.text)

    raw = { 'titles' : title,
            'singer' : singer }

    df = DataFrame(raw)
    df.to_excel("멜론힙합50_by_beautifulsoup.xlsx", encoding='utf-8')
