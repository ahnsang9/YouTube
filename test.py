import requests
import urllib.request
from bs4 import BeautifulSoup
import time
import re
from selenium import webdriver
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}

url = 'https://www.youtube.com/channel/UCpSFkW-1TFYy--Ag7__0w5A/videos'
result = requests.get(url, headers = header)
obj = BeautifulSoup(result.text, "html.parser")

titles = obj.select("div.style-scope ytd-section-list-renderer a")
#singers = obj.select("div.wrap_song_info div.rank02 span" )

print(titles)