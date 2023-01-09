import time
import unittest
import HTMLTestRunner
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Login(unittest.TestCase):

    EMAIL = (By.ID, "reg_email")
    PASSWORD = (By.ID, "reg_password")
    REGISTER_BTN = (By.NAME, "register")
    ERROR_TEXT = (By.XPATH,"//div[@id='content']//li[1]")
    PASSWORD_HINT = (By.XPATH, ".woocommerce-password-hint")
    DASHBOARD = (By.LINK_TEXT, "Dashboard")

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://demostore.supersqa.com/my-account/")
        self.driver.implicitly_wait(2)

    def test_register(self):
        self.driver.find_element(*self.EMAIL).send_keys("adresss@gmail.com")
        self.driver.find_element(*self.PASSWORD).send_keys("6KTPNqcwU#$Ae7PAD")
        self.driver.find_element(*self.REGISTER_BTN).click()

        try:
            self.driver.find_element(*self.DASHBOARD)
            print('Registered successfully')

        except NoSuchElementException:
            print("Registration has not been completed")

    def test_password_hint(self):
        self.driver.find_element(*self.EMAIL).send_keys("a071@gmail.com")
        self.driver.find_element(*self.PASSWORD).send_keys("1a")
        time.sleep(5)
        hint = self.driver.find_element(*self.PASSWORD_HINT).text
        expected_text = 'Hint: The password should be at least twelve characters long. To make it stronger, use upper and lower case letters, numbers, and symbols like ! " ? $ % ^ & ).'
        assert hint == expected_text, f"Error: expected: {expected_text}, actual: {hint}"

if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))