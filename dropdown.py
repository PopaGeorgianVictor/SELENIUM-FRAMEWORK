import time
import unittest
import HTMLTestRunner
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Dropdown(unittest.TestCase):
    DROPDOWN_CLASS= (By.ID, 'coding-language-select')
    DROPDOWN_CSS = (By.ID, "dropdownMenuButton")
    OPTION_CSS = (By.LINK_TEXT, 'PORTOFOLIO')

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
        dropdown_object.select_by_value('Java')
        dropdown_object.select_by_value('PHP')
        dropdown_object.select_by_value('C#')
        dropdown_object.select_by_value('SQL')

    def test_class_all_option(self):
        my_dropdown = self.driver.find_element(*self.DROPDOWN_CLASS).click()
        dropdown_object = Select(my_dropdown)

        all_options = dropdown_object.options
        for option in all_options:
            print(option.text)

    def test_css_all_option(self):
        self.driver.find_element(*self.DROPDOWN_CSS).click()
        self.driver.find_element(*self.OPTION_CSS).click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        print("Second window title = " + self.driver.title)

        try:
            self.driver.find_element(By.CSS_SELECTOR, "span[title='PORTOFOLIO']")
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")


if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))