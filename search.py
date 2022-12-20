import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import ActionChains

class Sliders(unittest.TestCase):

    SEARCH_BAR = (By.ID,"myInput")
    ELEM = (By.XPATH, "//a[normalize-space()='LISTS']")


    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/search_bar")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_search(self):
        self.driver.find_element(*self.SEARCH_BAR).send_keys('lists')







if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))