'''from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=qRXtfk3NYeM')
yt_streams = yt.streams
yt.streams.filter(only_audio=True)
itag = 140
my_stream = yt_streams.get_by_itag(itag)
# my_stream.download('C:\\Users\82105\Desktop\YouTube','%s'%yt_title) #데탑
my_stream.download() #랩탑
def show_progress_bar(stream: Stream, chunk: bytes, bytes_remaining: int):
    return  # do work
print(yt.register_on_progress_callback(show_progress_bar))'''

import pandas as pd
from pydub import AudioSegment
import glob
import os
import eyed3
from tqdm import tqdm

xlsx = pd.read_excel('멜론플레이리스트_90-00.xlsx')
titles = xlsx['title']
singers = xlsx['singer']
albums = xlsx['album']


video_dir = 'C:\\Users\82105\Desktop\YouTube\90-00_mp4'
os.chdir(video_dir)

'''extension_list = ('*.mp4')
for extension in extension_list:'''
a = glob.glob('*.mp4')
for i in tqdm(range(len(a))):
    #mp3_filename = os.path.splitext(os.path.basename(a[i]))[0] + '.mp3'
    AudioSegment.from_file(a[i]).export('C:\\Users\82105\Desktop\YouTube\90-00_mp3', format='mp3')
print('변환중...')

for i in range(len(titles)):
    song = eyed3.load("C:\\Users\82105\Desktop\YouTube\%s.mp3" % titles[i])
    song.tag.title = '%s' % titles[i]
    song.tag.artist = '%s' % singers[i]
    song.tag.album = '%s' % albums[i]
    song.tag.save()



