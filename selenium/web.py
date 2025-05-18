from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
# from selenium.webdriver.chrome.service import Service
# service_obj=Service("https://rahulshettyacademy.com")
# driver=webdriver.Chrome(service=service_obj)
# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)
