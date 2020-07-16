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

driver = webdriver.Chrome('C:\\Users\안상훈\PycharmProjects\chromedriver.exe',chrome_options=options)
driver.get("https://member.melon.com/muid/web/login/login_inform.htm") #로그인 페이지
window_before = driver.window_handles[0] #메인 페이지를 before로 지정
windows_count1 = len(driver.window_handles)
driver.find_element_by_xpath('//*[@id="conts_section"]/div/div/div[1]/button/span').click() #카카오계정 로그인 버튼
while True:
    windows_count2 = len(driver.window_handles)
    if windows_count2 > windows_count1:
        driver.switch_to.window(driver.window_handles[-1])  # 로그인창 활성화
        break
    else: continue
element = driver.find_element_by_xpath('//*[@id="id_email_2"]')
element.send_keys(id)
element = driver.find_element_by_xpath('//*[@id="id_password_3"]')
element.send_keys(pw)
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click() #로그인 실행

driver.switch_to.window(window_before) #메인 페이지 활성화

while(True):
    try:
        driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[2]/li[1]/a/span[2]').click() #마이뮤직 버튼
        break
    except:pass
while(True):
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
print('원하는 플레이리스트 번호를 입력하세요 : ')
num = int(input())
driver.find_element_by_xpath('//*[@id="pageList"]/table/tbody/tr[%d]/td[2]/div/div/dl/dt/a'%num).click() #원하는 플레이리스트로 이동

'''while(True):
    try:
        driver.find_element_by_xpath('//*[@id="pageObjNavgation"]/div/span/a[1]').click() #2페이지로 넘어가기
        break
    except:pass
while(True):
    try:
        driver.find_element_by_xpath('//*[@id="pageObjNavgation"]/div/span/a[1]').click() #1페이지로 돌아오기
        break
    except:pass'''

titles = []
singers = []
albums = []

page = 1
id = driver.current_url[-9:]
back = '#params%5BplylstSeq%5D='
back2 = '&po=pageObj&startIndex='
fixed_current_playlist_url = 'https://www.melon.com/mymusic/playlist/mymusicplaylistview_inform.htm?plylstSeq=%s%s%s%s'%(id,back,id,back2)
while True:
    fd = fixed_current_playlist_url + '%d' % page
    driver.get(fd) #페이지 이동

    '''try:
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "pop_isms")))
    finally:
        pass'''
    time.sleep(1)
    title =  driver.find_elements_by_xpath('//*[@id="frm"]/div/table/tbody/tr/td[3]/div/div/a[1]/span')
    singer = driver.find_elements_by_id('artistName')
    album =  driver.find_elements_by_xpath('//*[@id="frm"]/div/table/tbody/tr/td[5]/div/div/a')
    if len(title) == 0:
        break
    for i in title:
        titles.append(i.text)
    for i in singer:
        singers.append(i.text)
    for i in album:
        albums.append(i.text)
    page += 50
    print("%d번째 하는중 . . ." %((page-1)/50))

df = pd.DataFrame({"title" : titles,
                   "singer" : singers,
                   "album" : albums})
df.to_excel("melon_%s_list.xlsx"%album_names[num-1])
album_name = album_names[num-1]
driver.quit()
print('playlist 다운 완료')