
from selenium import webdriver
# driver=webdriver.Chrome
from selenium.webdriver.chrome.service import Service
service_obj=Service("D:\Pragya Sharma\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)











