import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
a = session.get('https://www.youtube.com/channel/UC3SyT4_WLHzN7JmHQwKQZww', headers=headers)
print(a)
soup = BeautifulSoup(a.text, 'html.parser')
print(soup.select('#subscriber-count'))