import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import HTMLTestRunner

class Keyboard(unittest.TestCase):

    USERNAME = (By.ID, "logName")
    PASSWORD = (By.ID, "logPassword")

    def setUp(self) -> None:
        self.chrome = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.chrome.maximize_window()
        self.chrome.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/login_sign_up")
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_keys(self):
