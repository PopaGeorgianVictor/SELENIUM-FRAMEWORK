
import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Dropdown(unittest.TestCase):
    DROPDOWN_CLASS= (By.ID, 'coding-language-select')
    DROPDOWN_CSS = (By.ID, "dropdownMenuButton")
    OPTION_CSS = (By.XPATH, '//*[@id="dropdowns"]/div[2]/div/ul/li[4]/a')

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/dropdown")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_select_using_class(self):
        my_dropdown = self.driver.find_element(*self.DROPDOWN_CLASS)
        dropdown_object = Select(my_dropdown)
        dropdown_object.select_by_value('Python')

    def test_class_all_option(self):
        options = self.driver.find_elements(*self.DROPDOWN_CLASS)
        for option in options:
            print(option.text)


    def test_select_using_css(self):
        self.driver.find_element(*self.DROPDOWN_CSS).click()
        self.driver.find_element(*self.OPTION_CSS).click()

    def test_css_all_option(self):
        options = self.driver.find_elements(*self.DROPDOWN_CSS)
        for option in options:
            print(option.text)


if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))