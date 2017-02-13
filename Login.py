'''
Created on Feb 12, 2017

@author: Vaibhav
'''
from selenium.webdriver import chrome

if __name__ == '__main__':
    pass

from Helper.driver import *
from Helper.xpathList import *
from Helper.credentials import *

driver.get("https://www.instagram.com")
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Log In')))
driver.find_element_by_xpath(loginButtonText).click()
driver.find_element_by_xpath(userName).send_keys(uname)
driver.find_element_by_xpath(password).send_keys(pwd)
driver.find_element_by_xpath(loginButton).click()
delay = 3
driver.get("https://www.instagram.com/photato_head")


# elem = browser.find_element_by_link_text("Home")
# elem.click()