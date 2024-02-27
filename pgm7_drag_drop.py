import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains  # drag and drop

service = Service(executable_path='D:/mythili/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
#-------------
#------------
time.sleep(2)
source=driver.find_element(By.ID,"box3")
dest=driver.find_element(By.ID,"box103")
action=ActionChains(driver)
action.drag_and_drop(source,dest).perform()
# ------    extra   ------
print(source.get_attribute(By.ID))
if source.get_attribute(By.ID)=="box3" and dest.get_attribute(By.ID)=="box103":
    print("success")
else:
    print("failure")











                                                
