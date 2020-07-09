import requests
from pandas import Series, DataFrame
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}

url = "https://www.melon.com/genre/song_list.htm?gnrCode=GN0300"

result = requests.get(url, headers = header)
obj = BeautifulSoup(result.text, "html.parser")

temps = obj.select("div.wrap_song_info span a ")

temp = []
titles = []
singers =[]

for i in temps:
    temp.append(i.text)

titles = [temp[i] for i in range(0,len(temp)-1,2)]
singers = [temp[i] for i in range(1,len(temp),2)]
raw = { 'titles' : titles,
        'singer' : singers }

df = DataFrame(raw)
print(df)


