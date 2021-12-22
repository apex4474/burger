from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import csv
from bs4 import BeautifulSoup as bs
driver = webdriver.Chrome("C:\\Users\\apex4\\AppData\\Local\\Programs\\Python\\Python310\\WebDriver\\chromedriver.exe")
driver.get('https://map.kakao.com/')
time.sleep(1)
driver.refresh()
driver.find_element_by_id('search.keyword.query').send_keys('맥도날드')
time.sleep(1)
driver.find_element_by_id('search.keyword.query').send_keys(Keys.RETURN)
time.sleep(2)
driver.find_element_by_id("info.search.place.more").click()
time.sleep(2)
df = pd.DataFrame()
name = []
addr = []
lis = []
n=1;
for i in range(0,30):
    html = driver.page_source
    soup = bs(html,'html.parser')
    num = 14
    if i is 29:
        num = 10
    for j in range(0,num+1):
        string = soup.select(".link_name")[j].get_text()
        string = string.replace("맥도날드 ","")
        name.append(string)
        string = soup.select(".addr")[j].get_text()
        string = string.replace("\n","")
        addr.append(string)
    if n%5==0:
        driver.find_element_by_id("info.search.page.next").click()
        n=1
        time.sleep(3)
    else:
        n=n+1
        driver.find_element_by_id("info.search.page.no"+str(n)).click()
        time.sleep(2)

data = {
        '이름':name,
        '주소':addr
    }
df = pd.DataFrame(data)
print(df)
df.to_csv("macdonald.csv",mode = 'w', encoding="utf-8-sig")
