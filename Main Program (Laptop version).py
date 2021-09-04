from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

import random
from random import randint

FnamePATH = "C:/Users/boneb21/OneDrive - St Michael's College/Folder/Spam/FNames.txt"
LnamePATH = "C:/Users/boneb21/OneDrive - St Michael's College/Folder/Spam/LNames.txt"
RmessagePATH = "C:/Users/boneb21/OneDrive - St Michael's College/Folder/Spam/LMessages.txt"
PATH = "C:\Program Files (x86)\chromedriver.exe"


def spam():
    FnamePATH = "C:/Users/boneb21/OneDrive - St Michael's College/Folder/Spam/FNames.txt"
    LnamePATH = "C:/Users/boneb21/OneDrive - St Michael's College/Folder/Spam/LNames.txt"
    RmessagePATH = "C:/Users/boneb21/OneDrive - St Michael's College/Folder/Spam/LMessages.txt"
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
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


    number = 0
    while True:
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
            clickyear.click() #clicks what year level

            clicksubject = driver.find_element_by_name("checkbox-fc4a1db9-f695-499e-ac74-1f56e0c1edb9-field")
            clicksubject.click() #interested subjects

            clicktype = driver.find_element_by_name('checkbox-51a19ef7-d947-4ec6-a7da-239c2c821731-field')
            clicktype.click() #clicks on type of help


            actions = ActionChains(driver) 
            actions.send_keys(Keys.TAB)
            actions.perform()
            actions.perform()
            actions.perform()

            message = ActionChains(driver)
            Rmessage = random.choice(listOfmessages)
            rm = ' '.join(Rmessage)
            message.send_keys(rm) #General message
            message.perform()

            actions.perform()
                                    #Start anti bot
            PressEnter = ActionChains(driver)
            PressEnter.send_keys(Keys.ENTER)
            PressEnter.perform()
            time.sleep(.5)
            PressEnter.perform()

            input()             #Stop th ecode for a second
            PressEnter = ActionChains(driver)
            PressEnter.send_keys(Keys.ENTER)
            PressEnter.perform()
            time.sleep(.5)

            timedelay = 1000 * random.random()
            print(timedelay)
            time.sleep(timedelay)


            driver.refresh()
            time.sleep(.5)
            i += 1
        driver.close()
        time.sleep(5)
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get("https://www.wisortutoring.com/request-a-quote")
        return


spam()










