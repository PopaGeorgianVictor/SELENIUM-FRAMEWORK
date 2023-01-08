import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Login(unittest.TestCase):

    EMAIL = (By.ID, "reg_email")
    PASSWORD = (By.ID, "reg_password")
    REGISTER_BTN = (By.NAME, "register")
    ERROR_TEXT = (By.XPATH,"//div[@id='content']//li[1]")
    PASSWORD_HINT = (By.CSS_SELECTOR, ".woocommerce-password-hint")

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://demostore.supersqa.com/my-account/")
        self.driver.implicitly_wait(2)

    def test_insert_email(self):
        self.driver.find_element(*self.EMAIL).send_keys("test123@gmail.com")