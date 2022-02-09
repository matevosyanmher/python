import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r"C:\chromedriver_win32\chromedriver.exe")
driver.get('https://file-online.taxservice.am/')
# driver.delete_all_cookies()
driver.maximize_window()
time.sleep(4)

action = webdriver.ActionChains(driver)

driver.find_element(By.XPATH, '//*[@id="userName"]').send_keys('mhermf')
driver.find_element(By.XPATH, '//*[@id="tin"]').send_keys('02700078')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Mf101010$%')
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="mainForm:loginBtn"]').click()
element = driver.find_element(By.XPATH, '//*[@id="popupForm_notificationPanel:j_id16"]').click()

driver.find_element(By.XPATH, '//*[@id="prtab8"]/span/a').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Ֆիսկալ հաս').click()
driver.find_element(By.XPATH, '//*[@id="mainForm:j_id86"]').send_keys('51637105')

driver.find_element(By.XPATH, '//*[@id="mainForm:startDateInputDate"]').clear()
driver.find_element(By.XPATH, '//*[@id="mainForm:startDateInputDate"]').send_keys('22.12.2021')

driver.find_element(By.XPATH, '//*[@id="mainForm:endDateInputDate"]').clear()
driver.find_element(By.XPATH, '//*[@id="mainForm:endDateInputDate"]').send_keys('29.12.2021')
time.sleep(5)
element1 = driver.find_element(By.XPATH, '//*[@id="mainForm:j_id138"]')
action.move_to_element(element1).perform()
element1.click()

element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainForm:fiscalIncomes'
                                                                                     ':0:j_id202"]'))).click()
element3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@id='mainForm:fiscalIncomes:0:j_id202']"))).click()

