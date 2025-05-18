from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self,driver):
        self.driver=driver
        self.shop_link=(By.LINK_TEXT, "Shop")
        self.product_list=(By.CSS_SELECTOR, "div[class='card h-100']")
        self.cart_btn=(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    def add_to_cart(self,product_name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_list)
        for product in products:
            productname = product.find_element(By.XPATH, "div/h4/a").text
            if productname == product_name:
                product.find_element(By.CSS_SELECTOR, "button[class='btn btn-info']").click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_btn).click()

