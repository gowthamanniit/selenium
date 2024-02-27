import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
service = Service(executable_path='D:/mythili/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(3)
"""
#-----------------   working  -------------------
path=By.XPATH
key='/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
sb=driver.find_element(path,key)
sb.send_keys("admin")
"""
path=By.NAME
key='username'
sb=driver.find_element(path,key)
sb.send_keys("admin")


path2=By.NAME
key2='password'
driver.find_element(path2,key2).send_keys("admin@123")


path3=By.XPATH
key3='/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
driver.find_element(path3,key3).click()





                                                
