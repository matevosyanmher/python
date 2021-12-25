from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Opera()
# driver.get('https://www.amazon.com')
driver.get("https://www.geeksforgeeks.org/")
driver.delete_all_cookies()
# driver.maximize_window()
time.sleep(4)
action = webdriver.ActionChains(driver)

# get element
element = driver.find_element(By.XPATH, "//button[@class='gcse-search__btn not-expanded']")
action.click(element)

searchBar = driver.find_element(By.CLASS_NAME, "//i[@class='gfg-icon gfg-icon_search gfg-icon_white gcse-search__icon']")
# send keys
searchBar.send_keys("Arrays")
