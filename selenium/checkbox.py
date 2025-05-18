import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj=Service("D:\Pragya Sharma\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.implicitly_wait(5)
# driver.find_element(By.ID,"checkBoxOption1").click()
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value")=="option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radioButtons=driver.find_elements(By.CSS_SELECTOR,".radioButton")
radioButtons[1].click()
assert radioButtons[1].is_selected()

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()

action=ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

time.sleep(3)
driver.execute_script("window.scrollBy(0,500);")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("photo.png")



#headless or headmode
# chrome_options=webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
# chrome_options.add_argument("__ignore-certificate-errors")
# driver=webdriver.Chrome(service=service_obj,options=chrome_options)

time.sleep(10)






