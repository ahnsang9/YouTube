import taglib
#import ____melon_playlist_crawling as list
import ___YouTube_link_selenium as yt

#titles = list.titles
#singers = list.singers
#albums = list.albums
youtube_titles = yt.youtube_titles
for i in range(len(youtube_titles)):
    song = taglib.File("C:\\Users\안상훈\Desktop\youtube_download\%s.mp3"%youtube_titles[i])
    print(song.tags)