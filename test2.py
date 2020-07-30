from youtube_api import YoutubeDataApi

yt = YoutubeDataApi('AIzaSyCrtDBAVoMU0We-M7TIHDbGyuYGhQycqnA')

searches = yt.search(q='저스디스', max_results=1)
print('https://www.youtube.com/watch?v=' + searches[0]['video_id'])
