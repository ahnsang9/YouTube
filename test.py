from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Chrome('C:\\Users\안상훈\PycharmProjects\chromedriver.exe')

driver.get("https://member.melon.com/muid/web/login/login_inform.htm")

'''time.sleep(1)

albums = []
album =  driver.find_elements_by_xpath('//*[@id="frm"]/div/table/tbody/tr/td[5]/div/div/a')

for i in album:
    albums.append(i.text)

pd.set_option('display.max_colwidth', None)
df = pd.DataFrame({"album" : albums})
print(df)'''


