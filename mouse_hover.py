import  time
import unittest
import HTMLTestRunner
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class Hover(unittest.TestCase):
    MENU = (By.CSS_SELECTOR,"#container a")
    PORTOFOLIO = (By.LINK_TEXT, "Portofolio")
    ELEM = (By.LINK_TEXT, "PORTOFOLIO")

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PRESENTATION-SITE/")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_hover(self):
        menu = self.driver.find_element(*self.MENU)
        action = ActionChains(self.driver)
        action.move_to_element(menu).perform()
        link =  self.driver.find_element(*self.PORTOFOLIO)
        action.move_to_element(link).click().perform()
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





