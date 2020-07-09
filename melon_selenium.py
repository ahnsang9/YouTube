from selenium import webdriver
driver = webdriver.Chrome('C:\\Users\안상훈\PycharmProjects\chromedriver.exe')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

titles = []
singers = []
try:
    for page in range(10):
        if page == 0:
            driver.get("https://www.melon.com/genre/song_list.htm?gnrCode=GN0300")
        else:
            driver.find_element_by_xpath('//*[@id="pageObjNavgation"]/div/span/a[%d]' % page).click()

        try:
            element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, "pageObjNavgation"))
            )
        finally:
            pass

        title =  driver.find_elements_by_class_name('ellipsis.rank01')
        singer = driver.find_elements_by_class_name('ellipsis.rank02')

        for i in title:
            titles.append(i.text)
        for i in singer:
            singers.append(i.text)

    df = pd.DataFrame({"title" : titles,
                       "singer" : singers})


    df.to_excel("멜론힙합50_by_selenium.xlsx", encoding='utf-8')

finally:
    driver.quit()
'''
pd.set_option('display.max_colwidth', -1)
print(df)
'''
