from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(r"C:\chromedriver_win32\chromedriver.exe")
driver.get('https://www.amazon.com')
driver.delete_all_cookies()
time.sleep(4)

action = webdriver.ActionChains(driver)

# get element
element = driver.find_element(By.XPATH, "//*[@id='nav-link-accountList']")
action.move_to_element(element).perform()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="nav-flyout-ya-signin"]/a').click()
time.sleep(5)
# send keys
driver.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys("matevosyanmher@gmail.com")
driver.find_element(By.XPATH, '//*[@id="continue"]').click()
driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('Mh1101210101er')
driver.find_element(By.XPATH, '//*[@id="signInSubmit"]').click()
driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys('jenga')
driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Jenga Giant JS6 (Stacks to Over 4 Feet)').click()
driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]').click()
driver.find_element(By.XPATH, '//*[@id="sw-gtc"]/span/a').click()
driver.find_element(By.XPATH, '//*[@id="a-autoid-0-announce"]').click()
driver.find_element(By.XPATH, '//*[@id="quantity_1"]').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Delete Jenga Giant JS6 (Stacks to Over 4 Feet)').click()

# searchBar.send_keys("")
# driver.quit()
