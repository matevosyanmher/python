import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        s = Service(
            r"C:\Users\Mher Matevosyan\PycharmProjects\python\QA_Automation\SeleniumDasQA8\amazon\commons\operadriver"
            r".exe")
        self.driver = webdriver.Chrome(service=s)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        # elem = driver.find_element(By.NAME, 'q')
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source

    # def tearDown(self):
    #     self.driver.close()


if __name__ == "__main__":
    unittest.main()
