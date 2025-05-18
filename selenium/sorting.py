import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj=Service("D:\Pragya Sharma\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(5)
browserSortedlist=[]
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
veggieWebelement=driver.find_elements(By.XPATH,"//tr/td[1]")
for veggie in veggieWebelement:
    browserSortedlist.append(veggie.text)
originalList=browserSortedlist.copy()
browserSortedlist.sort()
assert originalList==browserSortedlist



time.sleep(5)