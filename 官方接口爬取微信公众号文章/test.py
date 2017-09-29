from selenium import webdriver
import json
import time

url = 'https://mp.weixin.qq.com/'
b = webdriver.Chrome()
b.get(url)
b.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[1]/div/span/input').clear()
b.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[1]/div/span/input').send_keys('cjxh19930616@sina.com')
b.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[2]/div/span/input').clear()
b.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[2]/div/span/input').send_keys('3291852a')
b.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[3]/label').click()
time.sleep(2)
b.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[4]/a').click()
time.sleep(15)
cookies = b.get_cookies()
cookie = {}

for i in cookies:
    cookie[i.get('name')] = i.get('value')

with open('cookies.txt','w') as c:
    json.dump(cookie,c)
b.close()