import pandas as pd
from pytube import YouTube
import __YouTube_link_selenium as link

album_name = link.album_name
data = pd.read_excel('%s_urls.xlsx'%album_name)
data = data['urls']
count = len(data)
for i in range(count):
    yt = YouTube(data[i])
    yt_streams = yt.streams
    yt.streams.filter(only_audio=True)
    itag = 140
    my_stream = yt_streams.get_by_itag(itag)
    my_stream.download('C:\\Users\안상훈\Desktop\youtube_download')
    print("%d중 %d개 완료"%(count, i+1))
print('완료')