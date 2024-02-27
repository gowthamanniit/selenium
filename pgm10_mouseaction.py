import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
service = Service(executable_path='D:/mythili/chromedriver-win64/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://support.orangehrm.com/portal/en/signin")
time.sleep(4)
driver.find_element(By.NAME,"username").send_keys("admin@gmail.com")
driver.find_element(By.NAME,"password").send_keys("admin@123")


"""
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
"""

