import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(4)

# login
enter_username = driver.find_element(By.ID,'user-name')
enter_username.send_keys('visual_user')
enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')
enter_password.send_keys('secret_sauce')
click_login_button = driver.find_element(By.CSS_SELECTOR, '#login-button')
click_login_button.click()
time.sleep(4)

# Click Add To Cart Button (backpack)
click_add_to_cart_sauce_labs_backpack_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
click_add_to_cart_sauce_labs_backpack_button.click()

# Click Add To Cart Button(Bike)
click_add_to_cart_sauce_labs_bike_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
click_add_to_cart_sauce_labs_bike_button.click()

# Click Add To Cart Button(bolt-t-shirt)
click_add_to_cart_sauce_labs_bolt_t_shirt_button = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
click_add_to_cart_sauce_labs_bolt_t_shirt_button.click()

# Click Add To Cart Button(Fleece Jacket)
click_add_to_cart_sauce_labs_fleece_jacket_button = driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-fleece-jacket')
click_add_to_cart_sauce_labs_fleece_jacket_button.click()

# Click Add to Cart Button(onesie)
click_add_to_cart_sauce_labs_onesie_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]')
click_add_to_cart_sauce_labs_onesie_button .click()

# Click Add To Cart Button(allthethings-t-shirt)
click_add_to_cart_sauce_labs_test_allthethings_t_shirt_button = driver.find_element(By.XPATH,'//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
click_add_to_cart_sauce_labs_test_allthethings_t_shirt_button.click()

# Click Shopping Cart Icon
click_cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
click_cart_button.click()

# Click Checkout Button
click_checkout_button = driver.find_element(By.ID, 'checkout')
click_checkout_button.click()

# Enter Customer Firstname
enter_firstname = driver.find_element(By.ID, 'first-name')
enter_firstname.send_keys('chi')

# Enter Customer Lastname
enter_lastname = driver.find_element(By.CSS_SELECTOR, '#last-name')
enter_lastname.send_keys('Oma')

# Enter Postal Code
enter_postalcode = driver.find_element(By.CSS_SELECTOR,'#postal-code')
enter_postalcode.send_keys("S7V0J2")
time.sleep(2)

# Click Continue Button
click_continue_button = driver.find_element(By.ID, 'continue')
click_continue_button.click()
time.sleep(2)

# Click Finish Button
click_finish_button = driver.find_element(By.ID, 'finish')
click_finish_button.click()
time.sleep(2)

# Click The Burger Menu Button
click_burger_menu_button = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
click_burger_menu_button.click()
time.sleep(2)

# Click Logout
click_logout_button = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
click_logout_button.click()
time.sleep(3)

driver.quit()

