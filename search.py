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

    def test_slide(self):
        slider = self.driver.find_element(*self.SLIDER)
        size = slider.size
        w = size['width']
        ActionChains(self.driver).drag_and_drop_by_offset(slider, w / 2, 0).perform()


if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))