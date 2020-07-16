import pandas as pd
from selenium import webdriver
import time
import ___melon_playlist_crawling as mp

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
album_name = mp.album_name
data = pd.read_excel('melon_%s_list.xlsx'%album_name)  # 플레이리스트 엑셀에서 데이터 불러오기
titles = data['title']
singers = data['singer']
albums = data['album']

urls = []
driver.get('https://www.youtube.com/')

for i in range(len(titles)):
    time.sleep(1)
    element = driver.find_element_by_name("search_query") #search창 지정
    element.clear() #search창 클리어
    #element.send_keys(f'{titles[i]} {singers[i]} {albums[i]}')
    element.send_keys(f'{titles[i]} {singers[i]} audio')
    driver.find_element_by_xpath('// *[ @ id = "search-icon-legacy"]').click()  # 검색버튼 클릭

    time.sleep(1)
    first = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/'
                                         'ytd-search/div[1]/ytd-two-column-search-'
                                         'results-renderer/div/ytd-section-list-renderer'
                                         '/div[2]/ytd-item-section-renderer/div[3]/ytd-video'
                                         '-renderer[1]/div[1]/div/div[1]/div/h3/a')
    driver.execute_script("arguments[0].click();", first)
    while(True):
            try:
                url = driver.current_url
                if url[:29] == 'https://www.youtube.com/watch':
                    urls.append(driver.current_url) #현재 페이지 url 복사
                    break
                else:continue
            except:pass

driver.close()
df = pd.DataFrame({'urls' : urls})
df.to_excel("%s_urls.xlsx"%album_name, encoding='utf-8')
print('url 다운 완료')