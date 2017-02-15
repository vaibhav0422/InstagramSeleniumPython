'''
Created on Feb 12, 2017

@author: Vaibhav
'''
from selenium.webdriver import chrome

from Helper.driver import *
from Helper.xpathList import *
from Helper.credentials import *
from time import sleep

driver.get("https://www.instagram.com")
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Log In')))
driver.find_element_by_xpath(loginButtonText).click()
driver.find_element_by_xpath(userName).send_keys(uname)
driver.find_element_by_xpath(password).send_keys(pwd)
print("Forced wait 2 Seconds")
sleep(2)
driver.find_element_by_xpath(loginButton).click()
sleep(3)
driver.get("https://www.instagram.com/photato_head") #<- My userName
followersNumber = driver.find_element_by_xpath(followers).get_attribute("title") #<- Get the follower Number.
print(followersNumber)