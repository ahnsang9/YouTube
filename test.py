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
'''import glob
import os

files = glob.glob('C:\\Users\82105\Desktop\YouTube\*.mp4')
for x in files:
    if not os.path.isdir(x):
        filename = os.path.splitext(x)
        try:
            os.rename(x,filename[0] + '.mp3')
        except:
            pass'''
import eyed3
from playsound import playsound
#playsound('C:\\Users\82105\Desktop\YouTube\\067. 런치-01-어떻게 지내 (답가).mp3')
for i in range(1):
    song = eyed3.load("C:\\Users\82105\Desktop\YouTube\\067. 런치-01-어떻게 지내 (답가).mp3")
    song = eyed3.load("Zeze.mp3")
    '''audiofile.tag.artist = "태티서"
    audiofile.tag.album = "holler"
    audiofile.tag.album_artist = "Various Artists"
    audiofile.tag.title = 'holler'
    audiofile.tag.track_num = 3
    audiofile.tag.save()'''

    song.tag.artist = "iu"
    song.tag.album = "zeze"
    song.tag.album_artist = "아이유"
    song.tag.title = 'zeze'
    song.tag.track_num = 3
    song.tag.save()


