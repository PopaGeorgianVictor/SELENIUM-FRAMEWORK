
import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

class Checkbox(unittest.TestCase):
    TO_SELECT_VALUE = '21-40'
    LOCATOR_BY_VALUE = f'input[name="age-group-checkbox"][value="{TO_SELECT_VALUE}"]'
    MY_CHOICE = (By.CSS_SELECTOR, LOCATOR_BY_VALUE)
    ALL_CHECKBOXES = (By.NAME, 'age-group-checkbox')

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/checkbox")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_select_one_checkbox(self):
        selected_ch =  self.driver.find_element(*self.MY_CHOICE)
        selected_ch.click()
        assert selected_ch.is_selected(), f"After clicking value {TO_SELECT_VALUE} it is not selected."

    def test_select_all_checkbokes(self):
        expected_number_of_options = 4
        all_ch = self.driver.find_elements(*self.ALL_CHECKBOXES)
        assert len(all_ch) == expected_number_of_options, "Number of checkboxes is not the expected"
        for checkbox in all_ch:
            checkbox.click()
            value = checkbox.get_attribute('value')
            if checkbox.is_selected():
                print(f"Checkbox with value '{value}' is selectable")
            else:
                raise Exception(f"Value '{value}' is not selectable")


if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))