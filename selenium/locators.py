import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service("D:\Pragya Sharma\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element(By.NAME,"email").send_keys("pragya@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("pragya")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("pragya")
dropdown=Select(driver.find_element(By.CSS_SELECTOR,"#exampleFormControlSelect1"))
dropdown.select_by_index(1)
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
# driver.find_element(By.CLASS_NAME,"ng-valid").send_keys("pragya")
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)



time.sleep(20)