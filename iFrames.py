import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Frames(unittest.TestCase):
    WITHOUT_FRAME = (By.ID, 'btnOutFrame')
    OF_FRAME =

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/iFrame")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_without_iFrame(self):
        self.driver.find_element(*self.WITHOUT_FRAME).click()
        alert = self.driver.switch_to.alert
        assert alert.text == 'Just Clicked Outside iFrame', "Should've gotten outside message"
        alert.dismiss()

    def test_of_iFrame(self):


