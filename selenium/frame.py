import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj=Service("D:\Pragya Sharma\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(5)
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am pragya vishwakarma and I am learning automation")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)


time.sleep(5)
