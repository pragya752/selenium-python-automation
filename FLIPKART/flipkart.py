import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.flipkart.com")
driver.implicitly_wait(5)
driver.maximize_window()

#HOME PAGE VALIDATIONS..............................
#LOGO,SEARCH BOX,LOGIN,CART,LOGIN ITEM LIST*********************************************

logo_element=driver.find_element(By.XPATH,"//img[@title='Flipkart']")
logo_is_visible=logo_element.is_displayed()
print("Flipkart logo is visible:",logo_is_visible)
search_element=driver.find_element(By.CSS_SELECTOR,"input[title='Search for Products, Brands and More']")
search_is_visible=search_element.is_displayed()
print(search_is_visible)
search_placeholder=search_element.get_attribute("placeholder")
assert search_placeholder=="Search for Products, Brands and More"
print(search_placeholder)
login_element=driver.find_element(By.CSS_SELECTOR,"a[title='Login']")
login_is_visible=login_element.is_displayed()
cart_element=driver.find_element(By.CSS_SELECTOR,"a[title='Cart']")
cart_is_visible=cart_element.is_displayed()
action=ActionChains(driver)
action.move_to_element(login_element).perform()
new_customer_element=driver.find_element(By.XPATH,"//span[text()='New customer?']")
new_customer_element.is_displayed()
login_itemlist_element=driver.find_elements(By.CSS_SELECTOR,"ul[class*='ecs1XG'] a[class='yx2hEq']")
expected_list=["My Profile","Flipkart Plus Zone","Orders","Wishlist","Rewards","Gift Cards"]
actual_list=[]
for element in login_itemlist_element:
    actual_list.append(element.text)
print(actual_list)
assert expected_list==actual_list

#HOME PAGE DIFFERENT PRODUCT SECTION VALIDATION*************************************************************************

driver.find_element(By.XPATH,"//img[@title='Flipkart']").click()
electronic_element_list=driver.find_elements(By.XPATH,"//div[text()='Best of Electronics']/parent::div/parent::div/parent::div/following-sibling::div//div[@class='_25HC_u']")
assert len(electronic_element_list)>=1
for item in electronic_element_list:
    print(item.text)

#ADDRESS VALIDATION*****************************************************************************************************

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
expected_address_text="Flipkart Internet Private Limited,\nBuildings Alyssa, Begonia &\nClove Embassy Tech Village,\nOuter Ring Road, Devarabeesanahalli Village,\nBengaluru, 560103,\nKarnataka, India\nCIN : U51109KA2012PTC066107\nTelephone: 044-45614700 / 044-67415800"
address_text=driver.find_element(By.XPATH,"//div[text()='Registered Office Address:']/following-sibling::div").text
print(address_text)
assert expected_address_text==address_text


#CONTACT US VALIDATION**************************************************************************************************

contact_us_element=driver.find_element(By.XPATH,"//a[text()='Contact Us']")
contact_url=contact_us_element.get_attribute("href")
driver.execute_script("window.open();")
wh=driver.window_handles
driver.switch_to.window(wh[1])
driver.get(contact_url)
assert "helpcentre" in driver.current_url
driver.find_element(By.XPATH,"//h1[text()='Flipkart Help Center | 24x7 Customer Care Support']").is_displayed()
driver.close()
driver.switch_to.window(wh[0])
# time.sleep(500)

#CLOSING THE LOGIN MODAL WINDOW*****************************************************************************************
try:
    login_pop_up_element=driver.find_element(By.CSS_SELECTOR,"span[class*=_30XB9F]")
except:
    print("Login popup is not displayed")
else:
    login_pop_up_element.click()


#LOGIN BY MANUALLY ENTERING OTP*****************************************************************************************

driver.find_element(By. CSS_SELECTOR,"a[title='Login']").click()
driver.find_element(By.CSS_SELECTOR,"input[class*=r4vIwl]").send_keys("***********")
driver.find_element(By.XPATH,"//button[text()='Request OTP']").click()
time.sleep(25)
# driver.find_element(By.XPATH,"//button[text()='Verify']").click()
user_element=driver.find_element(By.CSS_SELECTOR,"a[class='_1TOQfO'] span")
assert user_element.text=="Pragya"



#ADDING PRODUCT TO CART FROM NAV BAR***********************************************************************************
#VALIDATING PRODUCT PRICE FROM LIST PAGE AND PRODUCR DETAIL PAGE,SELECTING SIZE ADDING TO CART*************************

fashion_element=driver.find_element(By.CSS_SELECTOR," img[alt='Fashion']")
action.move_to_element(fashion_element).perform()
women_ethnic_element=driver.find_element(By.XPATH,"//*[text()='Women Ethnic']")
action.move_to_element(women_ethnic_element).perform()
kurta_kurti_element=driver.find_element(By.XPATH,"//*[text()='Women Kurtas & Kurtis']")
kurta_kurti_element.click()
url=driver.current_url
print(url)
assert "women-kurtas-and-kurtis" in url
search_text=driver.find_element(By.CSS_SELECTOR,"input[title='Search for products, brands and more']").get_attribute("value")
assert search_text=="kurtas kurtis"
result_text=driver.find_element(By.CSS_SELECTOR,"span[class='BUOuZu']").text
assert  "kurtas kurtis" in result_text
first_kurti_element=driver.find_element(By.CSS_SELECTOR,"div[class*='LFEi7Z']")
first_kurti_price=driver.find_element(By.XPATH,"//div[contains(@class,'LFEi7Z')]//div[@class='Nx9bqj']").text.replace("₹","")
print(first_kurti_price)
first_kurti_element.click()
wh=driver.window_handles
driver.switch_to.window(wh[1])
time.sleep(4)
kurti_detail_price=driver.find_element(By.CSS_SELECTOR,"div[class*='CxhGGd']").text.replace("₹","")
print(kurti_detail_price)
assert first_kurti_price==kurti_detail_price
kurti_size_M=driver.find_element(By.XPATH,"//li/a[text()='M']")

if kurti_size_M.is_enabled():
    kurti_size_M.click()
else:
    kurti_sizes_element=driver.find_elements(By.XPATH,"//ul/li/a[contains(@class,'zmLe5G')]")
    for size in kurti_sizes_element:
        if size.is_enabled():
            size.click()
            break
kurti_detail_price=driver.find_element(By.CSS_SELECTOR,"div[class*='CxhGGd']").text.replace("₹","")

add_to_cart_element=driver.find_element(By.XPATH,"//button[contains(@class,'In9uk2')]")
driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_element)
add_to_cart_element.click()


#ADDING PRODUCT TO CART AFTER SEARCHING THE PRODUCT********************************************************************
#VALIDATING PRODUCT PRICE FROM LIST PAGE AND PRODUCR DETAIL PAGE,SELECTING SIZE ADDING TO CART*************************

driver.find_element(By.CSS_SELECTOR,"input[title='Search for products, brands and more']").send_keys("shoes for women")
driver.find_element(By.CSS_SELECTOR,"button[class='MJG8Up']").click()
first_product_element=driver.find_element(By.XPATH,"//div[@class='_75nlfW']//div[contains(@class,'LFEi7Z')]")
first_product_price=first_product_element.find_element(By.XPATH,"//div[contains(@class,'Nx9bqj')]").text.replace("₹","")
print(first_product_price)
first_product_element.click()
wh=driver.window_handles
driver.switch_to.window(wh[2])
time.sleep(4)
product_detail_price=driver.find_element(By.CSS_SELECTOR,"div[class*='CxhGGd']").text.replace("₹","")
print(product_detail_price)
assert first_product_price==product_detail_price
product_size_7=driver.find_element(By.CSS_SELECTOR,"ul[class*='hSEbzK'] #swatch-3-size")

if product_size_7.is_enabled():
    product_size_7.click()
else:
    product_sizes_element=driver.find_elements(By.XPATH, "//ul/li/a[contains(@class,'zmLe5G')]")
    for size in product_sizes_element:
        if size.is_enabled():
            size.click()
            break
product_detail_price=driver.find_element(By.CSS_SELECTOR,"div[class*='CxhGGd']").text.replace("₹","")

time.sleep(4)
driver.find_element(By.XPATH,"//button[contains(@class,'In9uk2')]").click()
time.sleep(4)


#VALIDATION OF NUMBER OF PRODUCTS ADDED TO CART************************************************************************

cart_list_element=driver.find_elements(By.XPATH,"//div[contains(@class,'cPHDOP')]/div[contains(@class,'pk3Guc')]")
assert len(cart_list_element)==2


#RETRIEVING PLATFORM FEEE & DELIVERY CHARGE FROM THE CART***************************************************************

amount_list_element=driver.find_elements(By.CSS_SELECTOR,"span[class='b5rp0W']")
platform_fee=amount_list_element[2].text.replace("₹","")
delivery_charges=0 if amount_list_element[3].text=="Free" else amount_list_element[3].text.replace("₹","")
print(platform_fee, delivery_charges)


#VALIDATING EXPECTED AMOUNT AND ACTUAL AMOUNT***************************************************************************

expected_amount=sum([int(kurti_detail_price),int(product_detail_price),int(platform_fee),int(delivery_charges)])
actual_amount=driver.find_element(By.XPATH,"//div[@class='_1Y9Lgu']//div[@class='_1Y9Lgu']").text.replace("₹","")
print(expected_amount,actual_amount)
actual_amount=int(actual_amount)
assert expected_amount==actual_amount

#PLACING THE ORDER******************************************************************************************************

place_order_element=driver.find_element(By.XPATH,"//span[text()='Place Order']")
place_order_element.click()


time.sleep(2)