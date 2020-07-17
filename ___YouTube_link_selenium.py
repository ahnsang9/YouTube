from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pytube import YouTube
import time
import pandas as pd
import glob
import os.path
#import ____melon_playlist_crawling as mp

####################################################################################################################
download_path = 'C:\\Users\안상훈\Desktop\youtube_download'
####################################################################################################################

options = webdriver.ChromeOptions()
# headless 옵션 설정
#options.add_argument('headless')
#options.add_argument("no-sandbox")
# 브라우저 윈도우 사이즈
options.add_argument('window-size=1920x1080')
# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재

driver = webdriver.Chrome('C:\\Users\안상훈\PycharmProjects\chromedriver.exe',chrome_options=options)
#driver = webdriver.Chrome(mp.driver_path,chrome_options=options)
#list_name = mp.list_name
#data = pd.read_excel('멜론플레이리스트_%s.xlsx'%list_name)  # 플레이리스트 엑셀에서 데이터 불러오기
data = pd.read_excel('멜론플레이리스트_힙.xlsx')
titles = data['title']
singers = data['singer']
albums = data['album']

driver.get('https://www.youtube.com/')

action = ActionChains(driver) #단축키 보내기
mute = 0
urls = []
for i in range(len(titles)):
    element = driver.find_element_by_name("search_query") #search창 지정
    element.clear() #search창 클리어
    element.send_keys(f'{titles[i]} {singers[i]} official audio mp3')
    driver.find_element_by_xpath('// *[ @ id = "search-icon-legacy"]').click() #검색버튼 클릭

    time.sleep(1)
    first = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a')
    driver.execute_script("arguments[0].click();", first)
    time.sleep(1)
    while(True):
            try:
                url = driver.current_url
                if mute == 0:
                    time.sleep(1)
                    action.send_keys('m').perform() #단축키 m으로 음소거
                    mute = 1
                if url[:29] == 'https://www.youtube.com/watch':
                    urls.append(driver.current_url) #현재 페이지 url 복사
                    break
                else:continue
            except:pass
driver.quit()

for i in range(len(titles)):
    yt = YouTube(urls[i])
    yt_streams = yt.streams
    yt.streams.filter(only_audio=True)
    itag = 140
    my_stream = yt_streams.get_by_itag(itag)

    # my_stream.download('C:\\Users\82105\Desktop\YouTube') #데탑
    my_stream.download(download_path) #랩탑
    print('%s 완료...'%titles[i])

files = glob.glob(download_path + "\*.mp4")
for x in files:
    if not os.path.isdir(x):
        filename = os.path.splitext(x)
        try:
            os.rename(x,filename[0] + '.mp3')
        except:
            pass

print('\n***** 변환완료 *****\n')