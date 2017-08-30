# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from pprint import pprint

# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     # print(browser.current_url)
#     # print(browser.get_cookies())
#     # print(browser.page_source)
#     with open('baidu.txt','w',encoding='utf-8') as b:
#         b.write(browser.page_source)
# finally:
#     browser.close()

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
with open('taobao.html','w',encoding='utf-8') as b:
    b.write(browser.page_source)
browser.close()