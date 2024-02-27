import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
service = Service(executable_path='D:/mythili/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com/")
#-------------
webtitle=driver.title
print("website title:",webtitle)
if webtitle=="Google":
    print("title ok")
else:
    print("title not ok")
#------------
mydata=input("enter your searching data..")
driver.find_element(By.ID,'APjFqb').send_keys(mydata)
time.sleep(3)
driver.find_element(By.CLASS_NAME,"gNO89b").click()



                                                
