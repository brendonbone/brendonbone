from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from capmonster_python import NoCaptchaTaskProxyless

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import random
from random import randint


FnamePATH = "C:/DEV/brendonbone/FNames.txt"
LnamePATH = "C:/DEV/brendonbone/LNames.txt"
RmessagePATH = "C:/DEV/brendonbone/LMessages.txt"
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

website_key = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"
website_url = driver.current_url    

driver.get("https://www.wisortutoring.com/request-a-quote")


FnameFile = open(FnamePATH, 'r')    #preps list of first names
listOfFirstNames = []
for line in FnameFile:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    listOfFirstNames.append(line_list)

FnameFile.close()

LnameFile = open(LnamePATH, 'r')    #preps list of last names
listOfLastNames = []
for line in LnameFile:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    listOfLastNames.append(line_list)

LnameFile.close()

LmessagesFile = open(RmessagePATH, 'r')    #preps list of messages
listOfmessages = []
for line in LmessagesFile:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    listOfmessages.append(line_list)

LmessagesFile.close()


pressTAB = ActionChains(driver) #defines key presses
pressTAB.send_keys(Keys.TAB)

PressEnter = ActionChains(driver)
PressEnter.send_keys(Keys.ENTER)

pressControlT = ActionChains(driver)
pressControlT.send_keys(Keys.COMMAND + 't') 




def dissable_settings():
    driver.get("chrome://settings/content/protectedContent")
    pressTAB.perform()
    PressEnter.perform()
    pressTAB.perform()
    PressEnter.perform()
    driver.get("https://www.wisortutoring.com/request-a-quote")

dissable_settings()
number = 0
while True: #sets the forever loop
    i=0
    while i < 5:

        number += 1
        fname = random.choice(listOfFirstNames)
        fn = ''.join(fname)
        username = driver.find_element_by_name('fname')
        username.send_keys(fn) #Pick username for request
        
        lname = random.choice(listOfLastNames)
        ln = ''.join(lname)
        lastname = driver.find_element_by_name('lname')
        lastname.send_keys(ln) #Pick Lastname for request

        email = driver.find_element_by_name("email")
        email.send_keys(fn+ln+"@gmail.com") #Email used

        phonenumber = driver.find_element_by_id('number-e958992e-30bc-4c98-9e4e-1287524c046e-field')
        rnumber = randint(10000000, 99999999)
        rnumber = str(rnumber)
        phonenumber.send_keys("04"+rnumber) #Pick Phonenumber

        clickyear = driver.find_element_by_name("checkbox-1f8535df-fbb6-4af4-ac04-660f7ff8fc0b-field")       
        clickyear.click()  #clicks what year level

        

        clicksubject = driver.find_element_by_name("checkbox-fc4a1db9-f695-499e-ac74-1f56e0c1edb9-field")
        clicksubject.click()

    
        clicktype = driver.find_element_by_name('checkbox-51a19ef7-d947-4ec6-a7da-239c2c821731-field')
        clicktype.click() #clicks on type of help



        pressTAB.perform() #scrolls down to general message
        pressTAB.perform()

        pressTAB.perform()


        message = ActionChains(driver)
        Rmessage = random.choice(listOfmessages)
        rm = ' '.join(Rmessage)
        message.send_keys(rm) #General message
        message.perform()

        pressTAB.perform()
        pressTAB.perform()
        pressTAB.perform()
        pressTAB.perform()
        
        captcha = NoCaptchaTaskProxyless(client_key="da950b4af117f859d3c61d347e6472c0")
        taskId = captcha.createTask(website_url, website_key)
        print("# Task created successfully, waiting for the response.")
        response = captcha.joinTaskResult(taskId)
        print("# Response received.")
        driver.execute_script(f"document.getElementsByClassName('g-recaptcha-response')[0].innerHTML = '{response}';")
        print("# Response injected to secret input.")
        time.sleep(15)

        input()

        PressEnter.perform() 
        time.sleep(.5)
        PressEnter.perform()

        timedelay = 10 * random.random()
        print(timedelay)
        time.sleep(timedelay)

        time.sleep(.5)
        driver.refresh()
        time.sleep(.5)
        i += 1
    driver.close()
    time.sleep(5)
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.wisortutoring.com/request-a-quote")










