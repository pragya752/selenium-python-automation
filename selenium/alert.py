import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager




name="Pragya"
# service_obj=Service("D:\Pragya Sharma\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert=driver.switch_to.alert
print(alert.text)
assert name in alert.text
alert.accept()


time.sleep(10)