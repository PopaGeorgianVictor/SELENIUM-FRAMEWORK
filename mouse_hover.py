
import unittest
import HTMLTestRunner
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

class Hover(unittest.TestCase):
    MENU = (By.CSS_SELECTOR,"#container a")
    PORTOFOLIO = (By.XPATH, "//a[contains(text(),'Portofolio')]")


    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
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



if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))





