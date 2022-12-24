
import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import WebDriverException

class Radios(unittest.TestCase):
    LOCATOR_BY_VALUE = 'input[name="radio-stations"][value="{value}"]'
    RADIOS = (By.NAME, 'radio-stations')
    BTN1 = (By.CSS_SELECTOR, "input[value='magic fm']")
    BTN2 = (By.CSS_SELECTOR, "input[value='radio galaxy']")

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/radio_btn")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()


    def test_default_is_selected(self):
        expected_default_value = 'rock fm'
        default_element = self.driver.find_element(By.CSS_SELECTOR, self.LOCATOR_BY_VALUE.format(value=expected_default_value))
        assert default_element.is_selected(), f"The default value of {expected_default_value} is not selected."

    def test_elem_clickable(self):
        try:
            self.driver.find_element(*self.BTN1).click()
            print("Magic FM button is clickable")
        except WebDriverException:
            print("Magic FM button is not clickable")

        try:
            self.driver.find_element(*self.BTN2).click()
            print("Radio Galaxy button is clickable")
        except WebDriverException:
            print("Radio Galaxy button is not clickable")

    def test_verify_number_of_radio_btn(self):
        expected_values = ['magic fm','radio galaxy','europa fm','rock fm']
        all_radios = self.driver.find_elements(*self.RADIOS)
        assert len(all_radios) == len(expected_values), "the number of radios does not match the expected." \
                                                        "Expected: {}, Actual: {}".format(len(expected_values),
                                                                                          len(all_radios))


if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))
