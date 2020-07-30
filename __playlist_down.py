from selenium import webdriver
from pytube import YouTube
import time
import eyed3
import glob
import os
from pydub import AudioSegment
from tqdm import tqdm
import requests
import platform
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from selenium .webdriver.common.keys import Keys


def click(xpath, number):
    while 1:
        try:
            if number == 1:
                driver.find_element_by_xpath(xpath).click()
            else:
                driver.find_element_by_xpath(xpath)
            break
        except:pass


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('같은 폴더가 있습니다')


def bs_crawling(url, info):
    soup = BeautifulSoup(session.get(url,headers = headers).text,'html.parser')
    title = soup.select('#downloadfrm > div > div > div.entry > div.info > div.song_name')[0].text.replace('\n','').replace('\t','').replace('\r', '').replace('19금','')[2:]
    title = "".join(i for i in title if i not in "\/:*?<>|.,")
    info[0].append(title)
    info[1].append(soup.select('#downloadfrm > div > div > div.entry > div.info > div.artist')[0].text)
    info[2].append(soup.select('#downloadfrm > div > div > div.entry > div.meta > dl > dd:nth-child(2) > a')[0].text)
    info[3].append(soup.select('#downloadfrm > div > div > div.entry > div.meta > dl > dd:nth-child(6)')[0].text)
    info[4].append(soup.select('#downloadfrm > div > div > div.thumb > a > img')[0]['src'])
    try:
        info[5].append(soup.select('#d_video_summary')[0].get_text(separator='\n').replace('\t','').replace('\r',''))
    except:
        info[5].append([''])  # 19금은 로그인해야 가사 나옴 (bs4로는 어렵)



headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
session = requests.Session()

ID = 'ahnsang9@naver.com'
PW = 'wpgkrmfk1!'

if platform.node() == 'DESKTOP-DSPFGTE':
    driver_path = 'C:\\Users\82105\PycharmProjects\YouTube_git2\chromedriver.exe'
    download_path = 'C:\\Users\82105\Desktop\YouTube'
else:
    driver_path = 'C:\\Users\안상훈\PycharmProjects\chromedriver.exe'
    download_path = 'C:\\Users\안상훈\Desktop\youtube_download'

options = webdriver.ChromeOptions()
#options.add_argument('headless')  # headless 옵션 설정
#options.add_argument("no-sandbox")  # headless 옵션 설정
options.add_argument('window-size=1920x1080')  # 브라우저 윈도우 사이즈
options.add_argument("disable-gpu")  # 사람처럼 보이게 하는 옵션들 # 가속 사용 x
options.add_argument("lang=ko_KR")  # 사람처럼 보이게 하는 옵션들 # 가짜 플러그인 탑재

driver = webdriver.Chrome(driver_path,chrome_options=options)
before_login = len(driver.window_handles)  # 시작시 윈도우 수

driver.get("https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fclient_id%3D6cfb479f221a5adc670fe301e1b6690c%26redirect_uri%3Dhttps%253A%252F%252Fmember.melon.com%252Foauth.htm%26response_type%3Dcode%26state%3DtqwvR%2540t%252FeWbVEGGPRllAIOKVGlnYr9Vk7MMim6C6xG29W%2540ukELOWbfqLmL1bR1gkghWty%2540%252FFIc5D8FnDybJ%2540uA%253D%253D%26encode_state%3Dtrue")  # 멜론 로그인 페이지
click('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/fieldset/div[2]/div/label',1)
driver.find_element_by_xpath('//*[@id="id_email_2"]').send_keys(ID)
driver.find_element_by_xpath('//*[@id="id_password_3"]').send_keys(PW)
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click()  # 로그인 실행

while 1:
    if len(driver.window_handles) == before_login + 1:
        break  # 창 하나 더 생기면 관둠

driver.switch_to.window(driver.window_handles[-1])  # 새로생긴창 활성화
click('//*[@id="gnb_menu"]/ul[2]/li[1]/a/span[2]',1)  # 마이뮤직 버튼
click('//*[@id="conts"]/div[1]/ul/li[3]/a/span',1)  # 플레이리스트 버튼

list_names = [x.text for x in driver.find_elements_by_xpath('//*[@id="pageList"]/table/tbody/tr/td[2]/div/div/dl/dt/a')]
print(*list_names, sep='  ')
print('\n다운로드 원하는 playlist 번호를 입력하세요')
num = int(input())-1
number_of_songs = int(driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/table/tbody/tr[%d]/td[3]/div/p'%(num+1)).text[8:-1])
click('//*[@id="pageList"]/table/tbody/tr[%d]/td[2]/div/div/dl/dt/a'%(num+1),1)  # 원하는 플레이리스트로 이동
createFolder(download_path + '\%s'%list_names[num])


info = [[],[],[],[],[],[]]  # 제목, 가수, 앨범, 장르, 커버사진, 가사
url_id = driver.current_url[-9:]
for i in tqdm(range(number_of_songs//50+1),desc='플레이리스트 정보 다운중...'):
    driver.get('https://www.melon.com/mymusic/playlist/mymusicplaylistview_inform.htm?plylstSeq=%s#params%%5BplylstSeq%%5D=%s&po=pageObj&startIndex=%d' % (url_id, url_id, 50*i+1))  # 페이지 이동
    time.sleep(1)
    song_url = ['https://www.melon.com/song/detail.htm?songId=' + x.get_attribute('href')[36:-3] for x in driver.find_elements_by_class_name('btn_icon_detail')]
    for j in range(len(song_url)):
            bs_crawling(song_url[j],info)
            img_src = info[4][50*i+j]
            urlretrieve(img_src, download_path + '\%s'%list_names[num] + '\%s.jpg'%(info[0][50*i+j]))


driver.get('https://www.youtube.com/')
mute = 0
yt_urls = []
for i in tqdm(range(number_of_songs),desc='url 복사중..'):
    element = driver.find_element_by_name("search_query")  # search창 지정
    element.clear()  # search창 클리어
    element.send_keys(f'\"{info[0][i]} {info[1][i]}\" +audio +mp3 .video')
    time.sleep(0.1)
    element.send_keys(Keys.RETURN)  # 엔터
    time.sleep(0.9)
    yt_url_temp = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a').get_attribute('href')
    #a = int(input())
    #yt_url_temp = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[%d]/div[1]/ytd-thumbnail/a'%a).get_attribute('href')
    yt_urls.append(yt_url_temp)

driver.quit()


for i in tqdm(range(number_of_songs), desc='mp4 다운중..'):
    try:
        yt = YouTube(yt_urls[i])
        yt_streams = yt.streams.filter(only_audio=True)
        my_stream = yt_streams.get_by_itag(140)
        my_stream.download(download_path + '\%s' % list_names[num], '%s' %info[0][i])
    except:pass

os.chdir(download_path + '\%s' % list_names[num])
temp = glob.glob('*.mp4')
for i in tqdm(range(len(temp)),desc='mp4 -> mp3 변환중..'):
    mp3_filename = os.path.splitext(os.path.basename(temp[i]))[0] + '.mp3'
    AudioSegment.from_file(temp[i]).export(mp3_filename, format='mp3')

for i in range(number_of_songs):  # 태그 초기화
    try:
        song = eyed3.load(download_path + "\%s\%s.mp3" %(list_names[num], info[0][i]))
        song.tag.title = '%s' % info[0][i]
        song.tag.artist = '%s' % info[1][i]
        song.tag.album = '%s' % info[2][i]
        song.tag.track_num = i
        song.tag.images.set(3, open(download_path + "\%s\%s.jpg" %(list_names[num], info[0][i]), 'rb').read(), 'image/jpeg')
        song.tag.lyrics.set(info[5][i])
        song.tag.save(version=eyed3.id3.ID3_V2_3)
    except:
        print('%s 다운 실패'%info[0][i])
[os.remove(f) for f in glob.glob(download_path + "\%s"%list_names[num] +'\*.jpg')]
[os.remove(f) for f in glob.glob(download_path + "\%s"%list_names[num] +'\*.mp4')]
