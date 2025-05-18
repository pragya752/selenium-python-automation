from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class HomePage:
    def __init__(self,driver):
        self.driver=driver
        self.home_link=(By.CSS_SELECTOR, "a[class='nav-link']")
        self.name_input=(By.NAME, "name")
        self.email=(By.NAME, "email")
        self.password=(By.ID, "exampleInputPassword1")
        self.check=(By.ID, "exampleCheck1")
        self.option_dropdown=(By.ID, "exampleFormControlSelect1")
        self.radio_btn=(By.ID, "inlineRadio1")
        self.dob=(By.CSS_SELECTOR, "input[type='date']")
        self.submit=(By.CSS_SELECTOR, "input[type='submit']")
        self.successmsg=(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")
    def home(self):
        self.driver.find_element(*self.home_link).click()
        self.driver.find_element(*self.name_input).send_keys("pragya")
        self.driver.find_element(*self.email).send_keys("sharmapragya@gmail.com")
        self.driver.find_element(*self.password).send_keys("pragya")
        self.driver.find_element(*self.check).click()
        self.driver.implicitly_wait(3)
        dropdown = Select(self.driver.find_element(*self.option_dropdown))
        dropdown.select_by_index(1)
        self.driver.find_element(*self.radio_btn).click()
        self.driver.find_element(*self.dob).send_keys("30-12-2000")
        self.driver.find_element(*self.submit).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.successmsg))
        successtext = self.driver.find_element(*self.successmsg).text
        print(successtext)
