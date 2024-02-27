from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
service = Service(executable_path='D:/mythili/chromedriver-win64/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com/")

#view
mycookies=driver.get_cookies()
print("Total no. of cookies:",len(mycookies))
print(mycookies)

#add
acook={'name':'mythili','value':'password@123'}
driver.add_cookie(acook)

#view
mycookies=driver.get_cookies()
print("Total no. of cookies:",len(mycookies))
print(mycookies)

#delete cookie

driver.delete_cookie('mythili')

#view
mycookies=driver.get_cookies()
print("Total no. of cookies:",len(mycookies))
print(mycookies)


