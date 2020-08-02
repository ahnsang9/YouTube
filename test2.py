from youtube_search import YoutubeSearch

results = YoutubeSearch('저스디스', max_results=10).to_dict()
for i in range(len(results)):
        print(results[i]['duration'])
        print('https://www.youtube.com'+results[i]['url_suffix'])
