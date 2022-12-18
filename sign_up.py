import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import HTMLTestRunner


class Sign_up(unittest.TestCase):

    USERNAME = (By.ID, "signName")
    PASSWORD = (By.ID, "signPassword")
    EMAIL = (By.ID, "signEmail")
    SIGN_UP = (By.CSS_SELECTOR, "input[value='SignUp']")

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/login_sign_up#signup")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_empty_fields(self):
        self.driver.find_element(*self.SIGN_UP).click()
        expected_text = 'Please fill the required fields'
        errorMsg = self.driver.find_element(By.ID, 'errorMsg').text
        assert errorMsg == expected_text, f"Error: expected: {expected_text}, actual: {errorMsg}"




if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))



