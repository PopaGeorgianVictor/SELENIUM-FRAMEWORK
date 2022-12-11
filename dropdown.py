
import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Dropdown(unittest.TestCase):
    dropdown_class = (By.ID, 'coding-language-select')
    dropdown_css = (By.ID, "dropdownMenuButton")
    option_css = (By.XPATH, '//*[@id="dropdowns"]/div[2]/div/ul/li[4]/a')

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/dropdown")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_select_using_class(self):
        my_dropdown = self.driver.find_element(*self.dropdown_class)
        dropdown_object = Select(my_dropdown)
        dropdown_object.select_by_value('Python')

    def test_class_all_option(self):
        options = self.driver.find_elements(*self.dropdown_class)
        for option in options:
            print(option.text)


    def test_select_using_css(self):
        self.driver.find_element(*self.dropdown_css).click()
        self.driver.find_element(*self.option_css).click()

    def test_css_all_option(self):
        options = self.driver.find_elements(*self.dropdown_css)
        for option in options:
            print(option.text)


if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))