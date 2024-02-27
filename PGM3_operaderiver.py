#prerequest : must install mozilla firefox browser
from selenium import webdriver

from selenium.webdriver.edge.service import Service
#from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.chrome.service import Service

service=Service(executable_path="d:/mythili/msedgedriver.exe")
#service=Service(executable_path="d:/mythili/geckodriver.exe")
#service = Service(executable_path='D:/mythili/chromedriver.exe')

options=webdriver.EdgeOptions()
#options = webdriver.ChromeOptions()

driver=webdriver.Edge(service=service,options=options)

#driver=webdriver.Firefox(service=service,options=options)
#driver = webdriver.Chrome(service=service, options=options)
#driver.quit()

