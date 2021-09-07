from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import random
from random import randint

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

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
    driver.get("https://www.google.com/recaptcha/api2/demo")

dissable_settings()
delayTime = 2
audioToTextDelay = 10
