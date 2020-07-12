from selenium import webdriver
driver = webdriver.Chrome('C:\\Users\안상훈\PycharmProjects\chromedriver.exe')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from pytube import YouTube
pw = 'wpgkrmfk1!'

driver.get("https://www.melon.com/index.htm")
driver.find_element_by_xpath('//*[@id="gnbLoginDiv"]/div/button/span').click()
window_before = driver.window_handles[0]
driver.find_element_by_xpath('//*[@id="conts_section"]/div/div/div[1]/button/span').click()
while(True):
    try:
        window_after = driver.window_handles[1]
        break
    except:
        pass
driver.switch_to.window(window_after)
#login ~~~
driver.find_element_by_xpath('//*[@id="loginEmailField"]/div/label').click()
element = driver.find_element_by_xpath('//*[@id="id_email_2"]')
element.send_keys("ahnsang9@naver.com")
element = driver.find_element_by_xpath('//*[@id="id_password_3"]')
element.send_keys(pw)
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
driver.switch_to.window(window_before)
while(True):
    try:
        driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[2]/li[1]/a/span[2]').click()
        break
    except:
        pass

while(True):
    try:
        driver.find_element_by_xpath('//*[@id="conts"]/div[1]/ul/li[3]/a/span').click()
        break
    except:
        pass

while(True):
    try:
        driver.find_element_by_xpath('//*[@id="pageList"]/table/tbody/tr[1]/td[2]/div/div/dl/dt/a').click()
        break
    except:
        pass

titles = []
singers = []


for page in range(10):
    if page == 0:
        pass
    else:
        driver.find_element_by_xpath('//*[@id="pageObjNavgation"]/div/span/a[%d]' % page).click()

    try:
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "footer"))
        )
    finally:
        pass

    time.sleep(0.5)

    title =  driver.find_elements_by_class_name('ellipsis.rank01')
    singer = driver.find_elements_by_class_name('ellipsis.rank02')

    for i in title:
        titles.append(i.text)
    for i in singer:
        singers.append(i.text)

df = pd.DataFrame({"title" : titles,
                   "singer" : singers})


df.to_excel("멜론힙합50_by_selenium.xlsx", encoding='utf-8')


'''

