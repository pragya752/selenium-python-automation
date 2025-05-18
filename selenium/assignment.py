import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj=Service("D:\Pragya Sharma\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsOpened=driver.window_handles
driver.switch_to.window(windowsOpened[1])
userName=driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text
print(driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text)
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID,"username").send_keys(userName)
driver.find_element(By.ID,"password").send_keys("learning")
radiobuttons=driver.find_elements(By.CSS_SELECTOR,".radiotextsty")
radiobuttons[1].click()
driver.find_element(By.ID,"okayBtn").click()
driver.find_element(By.ID,"signInBtn").click()
time.sleep(3)

element=driver.find_element(By.CSS_SELECTOR,".alert-danger")
if element:
    print(element.text)


time.sleep(5)