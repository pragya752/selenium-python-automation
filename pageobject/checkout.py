from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkout_Confirmation:
    def __init__(self,driver):
        self.driver=driver
        self.checkout_btn=(By.CSS_SELECTOR, "button[class='btn btn-success']")
        self.name_input=(By.ID, "country")
        self.name_options=(By.LINK_TEXT, "India")
        self.checkbox=(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
        self.submit_btn=(By.CSS_SELECTOR, "input[type='submit']")
        self.successmsg=(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")
    def checkout(self):
        self.driver.find_element(*self.checkout_btn).click()

    def add_delivery_address(self,countryname):
        self.driver.find_element(*self.name_input).send_keys(countryname)
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located(self.name_options))
        self.driver.find_element(*self.name_options).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_btn).click()

    def validate_order(self):
        successmsg = self.driver.find_element(*self.successmsg).text
        print(successmsg)
