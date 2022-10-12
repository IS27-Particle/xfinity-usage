from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os.path import exists
import time
import requests
import datetime
import calendar
import pickle
import undetected_chromedriver as uc

########## Pre-Reqs
#Chrome Version 106.x
#wget https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_linux64.zip
#sudo unzip chromedriver_linux64.zip -d /usr/local/bin
#pip install selenium
#pip install pygsheets
#pip install pandas
#pip install undetected_chromedriver
#pip install requests

########## Manual Entries
BaseRate = 0.5
filePath = "/home/joe/Desktop/Usage.csv"
configPath = "/home/matt/.config/google-chrome/Default"
apiKey = "NFsjayXmu4Ls2VAwY95TK7ysRgftpGqw"
serverAddr = "192.168.1.11"
xUsername = "jwb1275@gmail.com"
xPassword = "ameengin11"

# Capture current Date Time
runtime = datetime.datetime.now()

# Gather Info from Syncthing
r = requests.get("http://"+serverAddr+":8384/rest/config/options", headers={"X-API-Key":apiKey,"Content-Type":"application/json"})
currMaxSend = r.json()['maxSendKbps']
currMaxRecv = r.json()['maxRecvKbps']
r = requests.get("http://"+serverAddr+":8384/rest/system/connections", headers={"X-API-Key":apiKey,"Content-Type":"application/json"})
currInTotal = r.json()['total']['inBytesTotal']/1024
currOutTotal = r.json()['total']['outBytesTotal']/1024

# Gather info from xFinity using selenium driver
options = uc.ChromeOptions()
#options.add_argument("--log-level=3")
options.add_argument("--user-data-dir="+configPath)
#options.headless = True
driver = uc.Chrome(options)
driver.get("https://login.xfinity.com/login")
time.sleep(5)
email_field = driver.find_element(By.ID, "user")
email_field.send_keys(xUsername)
email_field.submit()
time.sleep(10)
pwd_field = driver.find_element(By.ID, "passwd")
pwd_field.send_keys(xPassword)
pwd_field.submit()
time.sleep(10)
verification = driver.find_element(By.ID, "verificationCode")
if verification.size != 0: # Verification CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Will need to get and add cookies
    remember = driver.find_element(By.NAME, "remember_device")
    remember.click()
    code = input("Enter the verification code: ")
    verification.send_keys(code)
    verification.submit()
    time.sleep(10)

driver.get("https://www.xfinity.com/learn/internet-service/auth?CMP=ILC_Internet_dss-myaccount-dev_au")
time.sleep(15)
usage = int(driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div[2]/div/div/div[4]/div[1]/div/p/strong").text.removesuffix(" GB"))
driver.get("https://customer.xfinity.com/#/devices#usage")
time.sleep(15)
total = int(driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/section[2]/div/div/div[2]/div[2]/div[1]/div/div/div/p/span/b[2]").text.removesuffix("GB"))


# Date and Time Strings
date = str(runtime.month) + "/" + str(runtime.day) + "/" + str(runtime.year)
time = str(runtime.hour) + ":" + str(runtime.minute)

# Last day of current month
EOM = calendar.monthrange(runtime.year, runtime.month)[1]

data_remaining = total-usage

# Hour calculations
hours = EOM * 24
hour = (runtime.day - 1) * 24 + runtime.hour
hoursLeft = hours-hour+1

# Ratios and RateFactor
hRatio = hour/hours
uRatio = usage/total
Ratio = uRatio/hRatio
rateFactor = BaseRate * Ratio

# Algorithm
calculatedRate = ((total - usage)/hoursLeft * rateFactor)/60/60*1024*1024

# Write to CSV
f = open(filePath, "a")
if exists(filePath):
    f.write("Date,Time,ISP Usage (GB),Hours in Month,Total Data Budget,Data Remainging,Hour of month,hour/hours,Usage/Budget,ratio,Hours Left,RateFactor,Calculated (KBps),Current Max In+Out (KBps),Current Actual In+Out (KBps),BaseRate,"+str(BaseRate))
f.write(date+","+time+","+str(usage)+","+str(hours)+","+str(total)+","+str(data_remaining)+","+str(hour)+","+str(hRatio)+","+str(uRatio)+","+str(hoursLeft)+","+str(rateFactor)+","+str(calculatedRate)+","+str(currMaxRecv+currMaxSend)+","+str(currInTotal+currOutTotal))
f.close()