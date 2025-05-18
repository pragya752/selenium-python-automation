import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
service_obj=Service("D:\Pragya Sharma\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice")

#static dropdown
dropdown=Select(driver.find_element(By.ID,"dropdown-class-example"))
# dropdown.select_by_index(2)
# dropdown.select_by_visible_text(option3)
dropdown.select_by_value("option3")





time.sleep(20)