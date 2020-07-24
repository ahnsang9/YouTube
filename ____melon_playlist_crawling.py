from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pytube import YouTube
import time
import eyed3
import glob
import os
import subprocess

id = 'ahnsang9@naver.com'
pw = 'wpgkrmfk1!'

while 1:
    print('데탑이면 1 , 랩탑이면 2')
    num = int(input())
    if num == 1:
        driver_path = 'C:\\Users\82105\PycharmProjects\YouTube_git2\chromedriver.exe'
        download_path = 'C:\\Users\82105\Desktop\YouTube'
        break
    elif num == 2:
        driver_path = 'C:\\Users\안상훈\PycharmProjects\chromedriver.exe'
        download_pate = 'C:\\Users\안상훈\Desktop\youtube_download'
        break
    else:
        print('???\n')

options = webdriver.ChromeOptions()
# headless 옵션 설정
#options.add_argument('headless')
#options.add_argument("no-sandbox")
# 브라우저 윈도우 사이즈
options.add_argument('window-size=1920x1080')
# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재

driver = webdriver.Chrome(driver_path,chrome_options=options)
before_login = len(driver.window_handles) #시작시 윈도우 수
driver.get("https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fclient_id%3D6cfb479f221a5adc670fe301e1b6690c%26redirect_uri%3Dhttps%253A%252F%252Fmember.melon.com%252Foauth.htm%26response_type%3Dcode%26state%3DtqwvR%2540t%252FeWbVEGGPRllAIOKVGlnYr9Vk7MMim6C6xG29W%2540ukELOWbfqLmL1bR1gkghWty%2540%252FFIc5D8FnDybJ%2540uA%253D%253D%26encode_state%3Dtrue")
#멜론 로그인 페이지
while 1:
    try:
        element = driver.find_element_by_xpath('//*[@id="id_email_2"]')
        break #입력창 뜨면 관둠
    except:pass
element.send_keys(id)
element = driver.find_element_by_xpath('//*[@id="id_password_3"]')
element.send_keys(pw)
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click() #로그인 실행
while 1:
    if len(driver.window_handles) == before_login + 1:
        break #창 하나 더 생기면 관둠
driver.switch_to.window(driver.window_handles[-1]) #새로생긴창 활성화
while 1:
    try:
        driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[2]/li[1]/a/span[2]').click() #마이뮤직 버튼
        break
    except:
        pass
while 1:
    try:
        driver.find_element_by_xpath('//*[@id="conts"]/div[1]/ul/li[3]/a/span').click() #플레이리스트 버튼
        break
    except:pass

list_name = driver.find_elements_by_xpath('//*[@id="pageList"]/table/tbody/tr/td[2]/div/div/dl/dt/a')
list_names = []
k = 0
for i in list_name:
    k += 1
    list_names.append(i.text)
    print('%d : '%k + i.text)
print('\n다운로드 원하는 playlist 번호를 입력하세요 : ')
num = int(input())
print('\n')
driver.find_element_by_xpath('//*[@id="pageList"]/table/tbody/tr[%d]/td[2]/div/div/dl/dt/a'%num).click() #원하는 플레이리스트로 이동

titles = []
singers = []
albums = []

page = 1
count = 0
id = driver.current_url[-9:]
back = '#params%5BplylstSeq%5D='
back2 = '&po=pageObj&startIndex='
fixed_current_playlist_url = 'https://www.melon.com/mymusic/playlist/mymusicplaylistview_inform.htm?plylstSeq=%s%s%s%s'%(id,back,id,back2)
while 1:
    driver.get(fixed_current_playlist_url + '%d' % page) #페이지 이동
    '''try:
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "pop_isms")))
    finally:
        pass'''

    time.sleep(1)
    title =  driver.find_elements_by_xpath('//*[@id="frm"]/div/table/tbody/tr/td[3]/div/div/a[1]/span')
    if len(title) == 0:
        break
    singer = driver.find_elements_by_id('artistName')
    album =  driver.find_elements_by_xpath('//*[@id="frm"]/div/table/tbody/tr/td[5]/div/div/a')

    for i in title:
        titles.append(i.text)
    for i in singer:
        singers.append(i.text)
    for i in album:
        albums.append(i.text)
    page += 50
    count += len(title)
    print("%d개 완료"%count)

'''df = pd.DataFrame({"title" : titles,
                   "singer" : singers,
                   "album" : albums})
df.to_excel("멜론플레이리스트_%s.xlsx"%list_names[num-1])
list_name = list_names[num-1]
driver.quit()'''
print('\n*****playlist 다운 완료*****\n')

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
                    time.sleep(0.5)
                    action.send_keys('m').perform() #단축키 m으로 음소거
                    mute = 1
                if url[:29] == 'https://www.youtube.com/watch':
                    urls.append(driver.current_url) #현재 페이지 url 복사
                    print('url 다운중...')
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

    # my_stream.download('C:\\Users\82105\Desktop\YouTube','%s'%yt_title) #데탑
    my_stream.download(download_path,'%s'%titles[i]) #랩탑
    print('%s 완료...'%titles[i])

files = glob.glob(download_path + "\*.mp4")
for x in files:
    '''if not os.path.isdir(x):
        filename = os.path.splitext(x)
        try:
            os.rename(x,filename[0] + '.mp3')
        except:
            pass'''
    s = x.split('.')[0] + '.mp3'
    cmds = ['ffmpeg', '-i', x, '-vn', '-ab', '192K', '-y', s]
    subprocess.Popen(cmds)
    print('Converting', x, 'to', s)
for i in range(len(titles)):
    song = eyed3.load("C:\\Users\82105\Desktop\YouTube\%s.mp3" % titles[i])
    song.tag.title = ['%s' % titles[i]]
    song.tag.artist = ['%s' % singers[i]]
    song.tags.album = ['%s' % albums[i]]
    song.tag.save()
    print(song.tags)

print('\n***** 변환완료 *****\n')