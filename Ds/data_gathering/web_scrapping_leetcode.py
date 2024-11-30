from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:/Users/Acer/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')

driver = webdriver.Chrome(service=s)

driver.get('https://leetcode.com/problemset/?page=7')

elements = driver.find_elements(By.CSS_SELECTOR, '[role="row"]')

# html_code = []

# for element in elements:

#     html = element.get_attribute('outerHTML')
#     html_code.append(html)
    

html_code = driver.page_source
with open('leetcode_question.html','w',encoding='utf-8') as f:
    f.write(html_code)
