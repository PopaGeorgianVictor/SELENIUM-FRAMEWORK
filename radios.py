
import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Radios(unittest.TestCase):
    locator_by_value = 'input[name="radio-stations"][value="{value}"]'
    radios = (By.NAME, 'radio-stations')

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/radio_btn")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_default_is_selected(self):
        expected_default_value = 'rock fm'
        default_element = self.driver.find_element(By.CSS_SELECTOR, self.locator_by_value.format(value=expected_default_value))
        assert default_element.is_selected(), f"The default value of {expected_default_value} is not selected."

    def test_verify_number_of_radio_btn(self):
        expected_values = ['magic fm', 'radio galaxy', 'europa fm', 'rock fm']
        all_radios = self.driver.find_element(*self.radios)
        assert len(all_radios) == len(expected_values), "the number of radios does not match the expected." \
                                                        "Expected: {}, Actual: {}".format(len(expected_values),
                                                                                          len(all_radios))