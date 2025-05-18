# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions

from pageobject.login import LoginPage
from pageobject.home import HomePage
from pageobject.shop import ShopPage
from pageobject.checkout import Checkout_Confirmation

def test_e2e(browserinstances):
    driver=browserinstances
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.implicitly_wait(5)
    loginpage=LoginPage(driver)
    loginpage.login()
    homepage = HomePage(driver)
    homepage.home()
    shop_page=ShopPage(driver)
    shop_page.add_to_cart("Blackberry")
    shop_page.go_to_cart()
    checkout_confirmation=Checkout_Confirmation(driver)
    checkout_confirmation.checkout()
    checkout_confirmation.add_delivery_address("ind")
    checkout_confirmation.validate_order()


    # driver.find_element(By.CSS_SELECTOR,"span[class='navbar-toggler-icon']").click()




