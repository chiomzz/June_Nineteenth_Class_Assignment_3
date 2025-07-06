import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/inventory.html')
driver.maximize_window()
time.sleep(4)
driver.find_element(By.ID,'user-name').send_keys('visual_user')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
driver.find_element(By.CSS_SELECTOR, '#login-button').click()
time.sleep(4)
driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-fleece-jacket').click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
driver.find_element(By.XPATH,'//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
driver.find_element(By.ID, 'checkout').click()
driver.find_element(By.ID, 'first-name').send_keys('chi')
driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Oma')
driver.find_element(By.CSS_SELECTOR,'#postal-code').send_keys("S7V0J2")
time.sleep(2)
driver.find_element(By.ID, 'continue').click()
time.sleep(2)
driver.find_element(By.ID, 'finish').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link').click()
time.sleep(3)

