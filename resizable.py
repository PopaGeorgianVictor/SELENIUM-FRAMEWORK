import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import ActionChains

class Resize(unittest.TestCase):
    RESIZE = (By.XPATH, '//*[@id="resizable"]/div[3]')



    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/resizable")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_resizable(self):
        resizable = self.driver.find_element(*self.RESIZE)
        ActionChains(self.driver).drag_and_drop_by_offset(resizable, 500, 500).perform()

        # resize back
        ActionChains(self.driver).drag_and_drop_by_offset(resizable, -500, -500).perform()

        expected = {'width': 1550, 'height': 830}
        actual = self.driver.get_window_size()
        assert expected == actual , f"Error: expected: {expected}, actual: {actual}"

