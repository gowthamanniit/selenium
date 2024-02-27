import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='D:/mythili/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.youtube.com")
#----------------
while True:
    mysearch=input("Enter your searching data:")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").clear()
    searchbox=driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys(mysearch)
    searchbut=driver.find_element(By.ID,'search-icon-legacy')
    time.sleep(5)
    searchbut.click()
    ch=input("do you want to continue search y/n:")
    if ch=="n" or ch=="N":
        break
#----------------
print("bye")

                                                
