from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path="D:\Webdriver\chromedriver.exe")
# driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)
action = webdriver.ActionChains(driver)
driver.get("https://www.amazon.com")

accountAndList = driver.find_element(By.XPATH, "//*[@id='nav-link-accountList']")
action.move_to_element(accountAndList).perform()
recommendations = driver.find_element(By.LINK_TEXT, "Recommendations")
recommendations.click()
firstFoundItem = driver.find_element(By.XPATH, '//*[@id="gridItemRoot"]/div[1]')
firstFoundItem.click()
for i in range(1, 17):
    locator = "//*[@id='p13n-asin-index-" + str(i) + "']"
    firstFoundItem = driver.find_element(By.XPATH, locator)
    firstFoundItem.click()
    time.sleep(1)
