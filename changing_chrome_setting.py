from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

import random
from random import randint

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

pressTAB = ActionChains(driver)
pressTAB.send_keys(Keys.TAB)

pressENTER = ActionChains(driver)
pressENTER.send_keys(Keys.ENTER)


def dissable_settings():
    driver.get("chrome://settings/content/protectedContent")

    pressTAB.perform()
    pressENTER.perform()
    pressTAB.perform()
    pressENTER.perform()
    driver.close()


