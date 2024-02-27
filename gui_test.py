import time
import tkinter
from tkinter import ttk,messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
service = Service(executable_path='D:/mythili/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
win=tkinter.Tk()
wi=win.winfo_screenwidth()
he=win.winfo_screenheight()
#print(wi)
#print(he)
win.configure(width=wi,height=he,bg="pink")
def serfun():
    website=sertb.get()
    domain=dname.get()
    sdata=searchdata.get()
    driver.get("https://www."+website+domain)    
    #messagebox.showinfo("success","button clicked:"+data)
    driver.find_element(By.ID,'APjFqb').send_keys(sdata)
    time.sleep(3)
    driver.find_element(By.CLASS_NAME,"gNO89b").click()
    
tit=tkinter.Label(win,text="GUI - Selenium Test ",font=("arial",36),bg="red",fg="yellow")
tit.place(x=300,y=100)
serlbl=tkinter.Label(win,text="Enter Website Name:",font=("arial",25))
serlbl.place(x=10,y=200)
sertb=tkinter.Entry(win,font=("times",25))
sertb.place(x=340,y=200)
seldom=[".com",".in",".gov.in",".org",".edu"]

dname=ttk.Combobox(win,values=seldom,font=("times",22))
dname.place(x=700,y=200)

serelelbl=tkinter.Label(win,text="Enter Search Data",font=("arial",25))
serelelbl.place(x=10,y=300)

searchdata=tkinter.Entry(win,font=("arial",25))
searchdata.place(x=340,y=300)

serbut=tkinter.Button(win,text="Goto website",font=("arial",25),command=serfun)
serbut.place(x=500,y=400)
win.mainloop()
