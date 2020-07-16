import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Users\82105\PycharmProjects\YouTube_git2\chromedriver.exe')
action = ActionChains(driver)

driver.get('https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fclient_id%3D6cfb479f221a5adc670fe301e1b6690c%26redirect_uri%3Dhttps%253A%252F%252Fmember.melon.com%252Foauth.htm%26response_type%3Dcode%26state%3DtqwvR%2540t%252FeWbVEGGPRllAIOKVGlnYr9Vk7MMim6C6xG29W%2540ukELOWbfqLmL1bR1gkghWty%2540%252FFIc5D8FnDybJ%2540uA%253D%253D%26encode_state%3Dtrue')
'''time.sleep(1)
element = driver.find_element_by_name("search_query")
element.send_keys(f'사계 태연 official audio mp3')
driver.find_element_by_xpath('// *[ @ id = "search-icon-legacy"]').click()  # 검색버튼 클릭

time.sleep(1)

first = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/'
                                         'ytd-search/div[1]/ytd-two-column-search-'
                                         'results-renderer/div/ytd-section-list-renderer'
                                         '/div[2]/ytd-item-section-renderer/div[3]/ytd-video'
                                         '-renderer[1]/div[1]/div/div[1]/div/h3/a')
driver.execute_script("arguments[0].click();", first)
mute = 0
time.sleep(1)
while(True):
    try:
        if mute == 0:
            action.send_keys('m').perform()
            mute = 1
            break
        print('시도중',end='')
    except:
        print('시도중', end='')
        pass
'''