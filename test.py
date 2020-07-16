import pandas as pd
from selenium import webdriver
import time

driver = webdriver.Chrome('C:\\Users\82105\PycharmProjects\YouTube_git2\chromedriver.exe')
data = pd.read_excel('melon_힙_list.xlsx')  # 플레이리스트 엑셀에서 데이터 불러오기
titles = data['title']
singers = data['singer']
albums = data['album']

urls = []
driver.get('https://www.youtube.com/')
mute = 0
for i in range(len(titles)):
    time.sleep(1)
    element = driver.find_element_by_name("search_query") #search창 지정
    element.clear() #search창 클리어
    #element.send_keys(f'{titles[i]} {singers[i]} {albums[i]}')
    element.send_keys(f'{titles[i]} {singers[i]} mv official audio mp3')
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
    try:
        if mute == 0:
            driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[25]/div[2]/div[1]/span/button').click()
            mute = 1
    except: pass

    print('%d중 %d번째 url 추출 완료'%(len(titles),i+1))
driver.close()
df = pd.DataFrame({'urls' : urls})
df.to_excel("%s_urls.xlsx", encoding='utf-8')
print('url 다운 완료')