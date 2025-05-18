import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
service_obj=Service("D:\Pragya Sharma\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)
driver.find_element(By.ID,"username").send_keys("rahulshettyacademy")
driver.find_element(By.ID,"password").send_keys("learning")
driver.find_element(By.ID,"signInBtn").click()
driver.find_element(By.CSS_SELECTOR,"a[class='nav-link']").click()
driver.find_element(By.NAME,"name").send_keys("pragya")
driver.find_element(By.NAME,"email").send_keys("sharmapragya@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("pragya")
driver.find_element(By.ID,"exampleCheck1").click()
driver.implicitly_wait(3)
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
driver.find_element(By.ID,"inlineRadio1").click()
driver.find_element(By.CSS_SELECTOR,"input[type='date']").send_keys("30-12-2000")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']")))
successtext=driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']").text
print(successtext)
driver.find_element(By.LINK_TEXT,"Shop").click()
products=driver.find_elements(By.CSS_SELECTOR,"div[class='card h-100']")
for product in products:
    productname=product.find_element(By.XPATH,"div/h4/a").text
    if productname=="Blackberry":
        product.find_element(By.CSS_SELECTOR,"button[class='btn btn-info']").click()
time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"span[class='navbar-toggler-icon']").click()
driver.find_element(By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait=WebDriverWait(driver,20)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,"div[class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
successmsg=driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']").text
print(successmsg)


