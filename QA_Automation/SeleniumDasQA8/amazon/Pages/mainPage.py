from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def search_for_product(self, product):
        pass
