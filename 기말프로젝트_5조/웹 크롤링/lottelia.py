from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
driver = webdriver.Chrome("C:\\Users\\apex4\\AppData\\Local\\Programs\\Python\\Python310\\WebDriver\\chromedriver.exe")
driver.get("https://www.lotteria.com/Shop/Shop_List.asp")
name = []
addr = []
df = pd.DataFrame()
for j in range(1,132):
    num = 12
    if j == 131:
        num = 11
    for i in range(2,num):
        driver.find_element_by_xpath('//*[@id="devCallShopList"]/div[1]/div[2]/table/tbody/tr['+str(i)+"]/td[1]/a").click()
        driver.implicitly_wait(10)
        html = driver.page_source
        soup = bs(html,'html.parser')
        name.append(soup.select("h3")[0].string)
        addr.append(soup.select(".rt>span")[0].string)
        print(str(j) + "번째 "+soup.select("h3")[0].string)
        driver.find_element_by_xpath('//*[@id="btnList"]/img').click()
        driver.implicitly_wait(100)
    driver.execute_script("goPage("+str(j)+")")
    driver.implicitly_wait(1000)

data = {
        '이름':name,
        '주소':addr
    }
df = pd.DataFrame(data)
df.to_csv("lotteria.csv",mode = 'w', encoding="utf-8-sig")
