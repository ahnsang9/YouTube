import requests
from bs4 import BeautifulSoup
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
session = requests.Session()




info = [[],[],[],[],[],[]]  # 제목, 가수, 앨범, 장르, 커버사진, 가사
def bs_crawling(url,list):
    soup = BeautifulSoup(session.get(url,headers = headers).text,'html.parser')
    list[3].append(soup.select('#downloadfrm > div > div > div.entry > div.meta > dl > dd:nth-child(6)')[0].text)
    list[0].append(soup.select('#downloadfrm > div > div > div.entry > div.info > div.song_name')[0].text.replace('\n','').replace('\t','').replace('\r','')[2:])
    list[1].append(soup.select('#downloadfrm > div > div > div.entry > div.info > div.artist > a')[0].text)
    list[2].append(soup.select('#downloadfrm > div > div > div.entry > div.meta > dl > dd:nth-child(2) > a')[0].text)
    list[5].append(soup.select('#d_video_summary')[0].get_text(separator='\n').replace('\t','').replace('\r',''))
    list[4].append(soup.select('#downloadfrm > div > div > div.thumb > a > img')[0]['src'])


a = bs_crawling('https://www.melon.com/song/detail.htm?songId=106215',info)
a = bs_crawling('https://www.melon.com/song/detail.htm?songId=32183386',info)
print(info)
