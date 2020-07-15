import pandas as pd
import numpy as np
from selenium import webdriver
import time
from pytube import YouTube

data = pd.read_excel('melon_힙_list.xlsx')
data = data['urls']
'''
for i in data:
    #yt = YouTube('%s',%i)
    yt_streams = yt.streams
    yt.streams.filter(only_audio=True)
    itag = 140
    my_stream = yt_streams.get_by_itag(itag)
    my_stream.download('C:\\Users\안상훈\Desktop\youtube_download')'''