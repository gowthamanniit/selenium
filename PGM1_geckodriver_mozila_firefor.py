import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service(executable_path='D:/mythili/geckodriver.exe')
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)
#driver.get("https://www.google.com")
while True:
    ch=input("do you want stop search pls type no   otherwise type any key:")
    if ch=="No" or ch=="no" or ch=="NO" or ch=='nO':
        print("program end")
        break
    searchdata=input("enter your search data:")    
    driver.get("https://www.google.com/search?q="+searchdata)
#driver.get("https://www.google.com/search?q=gowthaman+niit&sca_esv=594548752&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiy49joybaDAxU4yqACHYtHA2QQ_AUoAnoECAIQBA&biw=433&bih=570&dpr=1")
#time.sleep(10)
#driver.quit()
