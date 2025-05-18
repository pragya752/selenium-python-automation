import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj=Service("D:\Pragya Sharma\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
#dynamic dropdown
driver.find_element(By.ID,"autosuggest").send_keys("Aus")
time.sleep(2)
countries=driver.find_elements(By.CSS_SELECTOR,"li[class= 'ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text== "Austria":
        country.click()
        break
print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

time.sleep(20)