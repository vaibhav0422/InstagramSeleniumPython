#Modify this file for setting the driver for diffferent browsers

from selenium import webdriver 
# from selenium.webdriver.common.keys import Keys
# import re

#Chrome Driver
chrome_path = r"C:\Users\Vaibhav\Downloads\sikuli\chromedriver_win32(1)\chromedriver.exe" #My path to chromedriver.exe
driver=webdriver.Chrome(chrome_path)

#Firefox Driver
#driver = webdriver.Firefox()
