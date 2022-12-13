import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import HTMLTestRunner

class Keyboard(unittest.TestCase):

    USERNAME = (By.ID, "signName")
    PASSWORD = (By.ID, "signPassword")
    EMAIL = (By.ID, "signEmail")

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/login_sign_up#signup")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()