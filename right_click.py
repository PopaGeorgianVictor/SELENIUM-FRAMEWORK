import time
import unittest
import HTMLTestRunner
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import ActionChains

class Right_Click(unittest.TestCase):

    CLICK = (By.CSS_SELECTOR, "#contextMenu a")
    ELEM =(By.LINK_TEXT,'PORTOFOLIO')

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/right_click_menu")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_right_click(self):
        ActionChains(self.driver).context_click().perform()
        self.driver.find_element(*self.CLICK).click()
        print('I clicked on OVERVIEW')
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        print("Second window title = " + self.driver.title)

        try:
            self.driver.find_element(*self.ELEM)
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")

if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))
