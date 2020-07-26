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


def click(xpath, number):
    while 1:
        try:
            if number == 1:
                driver.find_element_by_xpath(xpath).click()
            else:
                driver.find_element_by_xpath(xpath)
            break
        except:pass


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
driver.get("https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2"
           "Fauthorize%3Fclient_id%3D6cfb479f221a5adc670fe301e1b6690c%26redirect_uri%3Dhttps%"
           "253A%252F%252Fmember.melon.com%252Foauth.htm%26response_type%3Dcode%26state%3Dtqwv"
           "R%2540t%252FeWbVEGGPRllAIOKVGlnYr9Vk7MMim6C6xG29W%2540ukELOWbfqLmL1bR1gkghWty%2540%"
           "252FFIc5D8FnDybJ%2540uA%253D%253D%26encode_state%3Dtrue")  # 멜론 로그인 페이지

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
print(list_names)
print(*list_names, sep='\n')
while 1:
    print('\n다운로드 원하는 playlist 번호를 입력하세요')
    #num = int(input())-1
    num = 1
    if 0 <= num & num <= len(list_names)-1:
        break
    else:
        print('잘못 입력했습니다.')


number_of_songs = int(driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/table/tbody/tr[%d]/td[3]/div/p'%(num+1)).text[8:-1])
click('//*[@id="pageList"]/table/tbody/tr[%d]/td[2]/div/div/dl/dt/a'%(num+1),1)  # 원하는 플레이리스트로 이동


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('같은 폴더가 있습니다')
createFolder(download_path + '\%s'%list_names[num])

song_info = [[],[],[],[],[]]  # titles, singers, albums, image_urls, lyrics
titles = []
singers = []
albums = []
image_urls = []

page = 1
url_id = driver.current_url[-9:]
pbar = tqdm(total=number_of_songs,desc='플레이리스트 목록 다운중..')
while 1:
    driver.get('https://www.melon.com/mymusic/playlist/mymusicplaylistview_inform.htm?plylstSeq=%s'
               '#params%%5BplylstSeq%%5D=%s&po=pageObj&startIndex=%d' % (url_id, url_id, page))  # 페이지 이동
    time.sleep(1)
    title = driver.find_elements_by_xpath('//*[@id="frm"]/div/table/tbody/tr/td[3]/div/div/a[1]/span')
    singer = driver.find_elements_by_id('artistName')
    album = driver.find_elements_by_xpath('//*[@id="frm"]/div/table/tbody/tr/td[5]/div/div/a')

    name = []
    for i in title:
        titles.append(i.text)
        name.append(i.text)
    for i in singer:
        singers.append(i.text)
    for i in album:
        albums.append(i.text)

    temp = driver.find_elements_by_class_name('btn_icon_detail')
    temp_cover =[]
    lyrics = []
    for i in range(len(temp)):
        temp_cover.append('https://www.melon.com/song/detail.htm?songId=%d'%(int(temp[i].get_attribute('href')[36:-3])))
    for i in range(len(temp_cover)):
        driver.get(temp_cover[i])
        img = requests.get(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/form/div/div/div[1]/a/img').get_attribute('src'))
        with open(download_path + '\%s'%list_names[num] + '\%s.jpg'%(name[i]), 'wb') as writer:  # open for writing in binary mode
            writer.write(img.content)  # write the image
    page += 50
    pbar.update(len(title))
    if len(title) < 50:
        break
'''        lyrics.append(driver.find_elements_by_class_name('lyric'))
    for i in range(len(lyrics)):
        for j in range(len(lyrics[i])):
            lyrics[i][j] = lyrics[i][j].text
            print(lyrics[i][j])'''
pbar.close()


driver.get('https://www.youtube.com/')
mute = 0
yt_urls = []
for i in tqdm(range(len(titles)),desc='url 복사중..'):
    element = driver.find_element_by_name("search_query")  # search창 지정
    element.clear()  # search창 클리어
    element.send_keys(f'{titles[i]} {singers[i]} official audio mp3')
    click('//*[@id="search-icon-legacy"]',1)  # 검색버튼 클릭
    click('//*[@id="thumbnail"]/yt-img-shadow',2)
    time.sleep(1)
    yt_url_temp = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/'
                                               'ytd-two-column-search-results-renderer/div/ytd-section-list-'
                                               'renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-r'
                                               'enderer[1]/div[1]/ytd-thumbnail/a').get_attribute('href')
    yt_urls.append(yt_url_temp)
driver.quit()

for i in tqdm(range(len(titles)), desc='mp4 다운중..'):
    try:
        yt = YouTube(yt_urls[i])
        yt_streams = yt.streams
        yt.streams.filter(only_audio=True)
        my_stream = yt_streams.get_by_itag(140)
        my_stream.download(download_path + '\%s' % list_names[num], '%s' % titles[i])
    except:pass


os.chdir(download_path + '\%s' % list_names[num])
temp = glob.glob('*.mp4')
for i in tqdm(range(len(temp)),desc='mp4 -> mp3 변환중..'):
    mp3_filename = os.path.splitext(os.path.basename(temp[i]))[0] + '.mp3'
    AudioSegment.from_file(temp[i]).export(mp3_filename, format='mp3')


for i in range(len(titles)):  # 태그 초기화
    song = eyed3.load(download_path + "\%s\%s.mp3" %(list_names[num], titles[i]))
    song.tag.title = '%s' % titles[i]
    song.tag.artist = '%s' % singers[i]
    song.tag.album = '%s' % albums[i]
    song.tag.track_num = i
    song.tag.images.set(3, open(download_path + "\%s\%s.jpg" %(list_names[num], titles[i]), 'rb').read(), 'image/jpeg')
    song.tag.save(version=eyed3.id3.ID3_V2_3)
