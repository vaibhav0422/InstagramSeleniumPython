'''
Created on Feb 12, 2017

@author: Vaibhav
'''
# import unittest
# from selenium.webdriver import chrome
from Helper.driver import *
from Helper.xpathList import *
from Helper.credentials import *
from time import sleep
from Helper.handleNames import hNames
from random import randint


driver.get("https://www.instagram.com")
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Log In')))
driver.find_element_by_xpath(loginButtonText).click()
driver.find_element_by_xpath(userName).send_keys(uname)
driver.find_element_by_xpath(password).send_keys(pwd)
print("Forced wait 2 Seconds")
sleep(2)
driver.find_element_by_xpath(loginButton).click()
sleep(3)


wordLength = len(hNames)
for i in range(0,wordLength):
    hNameLocal = "https://www.instagram.com/"+ hNames[i]
    driver.get(hNameLocal)
    print("- Opening "+hNames[i]+"....")
    sleep(0.5 * randint(2,4))
    driver.find_element_by_xpath(followButton).click()
    print("- Followed "+hNames[i]+"....")
    print("-------------------------------")
    sleep(0.5 * randint (1,4))
    
driver.close()


# driver.get("https://www.instagram.com/photato_head") #<- My userName
# followersNumber = driver.find_element_by_xpath(followers).get_attribute("title") #<- Get the follower Number.
# print(followersNumber)