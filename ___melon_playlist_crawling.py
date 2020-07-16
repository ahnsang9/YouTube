from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

id = 'ahnsang9@naver.com'
pw = 'wpgkrmfk1!'

options = webdriver.ChromeOptions()
# headless 옵션 설정
options.add_argument('headless')
options.add_argument("no-sandbox")
# 브라우저 윈도우 사이즈
options.add_argument('window-size=1920x1080')
# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재

driver = webdriver.Chrome('C:\\Users\82105\PycharmProjects\YouTube_git2\chromedriver.exe',chrome_options=options) #크롬 실행
before_login = len(driver.window_handles) #시작시 윈도우 수
driver.get("https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fclient_id%3D6cfb479f221a5adc670fe301e1b6690c%26redirect_uri%3Dhttps%253A%252F%252Fmember.melon.com%252Foauth.htm%26response_type%3Dcode%26state%3DtqwvR%2540t%252FeWbVEGGPRllAIOKVGlnYr9Vk7MMim6C6xG29W%2540ukELOWbfqLmL1bR1gkghWty%2540%252FFIc5D8FnDybJ%2540uA%253D%253D%26encode_state%3Dtrue")
#로그인 페이지
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

album_name = driver.find_elements_by_xpath('//*[@id="pageList"]/table/tbody/tr/td[2]/div/div/dl/dt/a')
album_names = []
k = 0
for i in album_name:
    k += 1
    album_names.append(i.text)
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

df = pd.DataFrame({"title" : titles,
                   "singer" : singers,
                   "album" : albums})
df.to_excel("멜론플레이리스트_%s.xlsx"%album_names[num-1])
album_name = album_names[num-1]
driver.quit()
print('\nplaylist 다운 완료\n')