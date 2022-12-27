import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import ActionChains

class Resize(unittest.TestCase):
    RESIZE = (By.XPATH, '//*[@id="resizable"]/div[3]')
    ELEM_RESIZABLE = (By.ID, 'resizable')


    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/resizable")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_resizable(self):
        elem = self.driver.find_element(*self.ELEM_RESIZABLE)
        print("Original size is", elem.size)
        resizable = self.driver.find_element(*self.RESIZE)
        ActionChains(self.driver).drag_and_drop_by_offset(resizable, 500, 500).perform()
        print("After resize is", elem.size)

        expected_size = {'height': 619.0, 'width': 619.0}
        actual_size = elem.size
        assert expected_size == actual_size, f"Error: expected: {expected_size}, actual: {actual_size}"

        # resize back
        ActionChains(self.driver).drag_and_drop_by_offset(resizable, -500, -500).perform()


if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))