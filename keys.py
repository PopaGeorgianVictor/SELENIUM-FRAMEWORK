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
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/login_sign_up")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_keys(self):
        user = self.driver.find_element(*self.USERNAME)
        user.send_keys("my first login")
        user.send_keys(Keys.ENTER)
        expected_text = "Please fill the required fields"
        errorMsg = self.driver.find_element(By.ID, 'errorMsg').text
        assert errorMsg == expected_text, f"Error: expected: {expected_text}, actual: {rs_message}"
        user.send_keys(Keys.TAB)
        password = self.driver.find_element(*self.PASSWORD)
        password.send_keys("my first password")
        password.send_keys(Keys.BACKSPACE)
        password.send_keys("###hacking###")


