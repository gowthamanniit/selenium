import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
service = Service(executable_path='D:/mythili/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
#driver.switch_to.frame(1)
#driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
time.sleep(3)
#driver.switch_to.default_content()
driver.switch_to.frame(0)
driver.find_element(By.LINK_TEXT, "WebDriver").click()
time.sleep(3)


