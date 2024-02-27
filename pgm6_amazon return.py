import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
service = Service(executable_path='D:/mythili/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.amazon.com")

#time.sleep(3)

path=By.ID
key='twotabsearchtextbox'
sb=driver.find_element(path,key)
sb.send_keys("gents watch"+Keys.RETURN)




                                                
