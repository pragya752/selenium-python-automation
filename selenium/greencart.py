import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

expectedList=['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList=[]
service_obj=Service("D:\Pragya Sharma\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(results)
assert count>0
for result in results:
    actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()
assert expectedList==actualList
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

prices=driver.find_elements(By.XPATH,"//tbody/tr/td[5]")
summation=0
for price in prices:
    summation=summation +int(price.text)
print(summation)
totalAmount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert summation == totalAmount
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
time.sleep(5)
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
discountedAmount=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert totalAmount>discountedAmount




time.sleep(10)