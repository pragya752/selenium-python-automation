from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
service_obj=Service("D:\Pragya Sharma\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/upload-download-test/")
file_path="D:\Pragya Sharma\Downloads\download.xlsx"
driver.implicitly_wait(5)
driver.find_element(By.ID,"downloadButton").click()
file_input=driver.find_element(By.CSS_SELECTOR,"input[type='file']")
file_input.send_keys(file_path)

wait=WebDriverWait(driver,5)
successtext=(By.XPATH,"//div[text()='Updated Excel Data Successfully']")
wait.until(expected_conditions.visibility_of_element_located(successtext))
print(driver.find_element((By.XPATH,"//div[text()='Updated Excel Data Successfully']")).text)

