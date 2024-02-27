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
ansdic={"box1":"box101","box2":"box102","box3":"box103","box4":"box104","box5":"box105","box6":"box106","box7":"box107"}
qdis={"box1":"box101","box2":"box102","box3":"box105","box4":"box103","box5":"box106","box6":"box107","box7":"box104"}
v=qdis.keys()
v=list(v)
correct=0
wrong=0
for i in range(len(qdis)):
    time.sleep(2)
    source=driver.find_element(By.ID,v[i])
    dest=driver.find_element(By.ID,qdis[v[i]])
    action=ActionChains(driver)
    action.drag_and_drop(source,dest).perform()
    if qdis[v[i]]==ansdic[v[i]]:
        correct+=1
    else:
        wrong+=1
print("success count : ",correct)
print("failure count  : ",wrong) 
# ------    extra   ------
"""
print(source.get_attribute(By.ID))
if source.get_attribute(By.ID)=="box3" and dest.get_attribute(By.ID)=="box103":
    print("success")
else:
    print("failure")

"""









                                                
