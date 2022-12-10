
import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

class Checkbox(unittest.TestCase):
    to_select_value = '21-40'
    locator_by_value = f'input[name="age-group-checkbox"][value="{to_select_value}"]'
    my_choice = (By.CSS_SELECTOR, locator_by_value)
    all_checkboxes = (By.NAME, 'age-group-checkbox')

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/checkbox")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_select_one_checkbox(self):
        selected_ch =  self.driver.find_element(*self.my_choice)
        selected_ch.click()
        assert selected_ch.is_selected(), f"After clicking value {to_select_value} it is not selected."

    def test_select_all_checkbokes(self):
        expected_number_of_options = 4
        all_ch = self.driver.find_elements(*self.all_checkboxes)
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