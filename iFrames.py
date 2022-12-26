import time
import unittest
import HTMLTestRunner
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Frames(unittest.TestCase):
    WITHOUT_FRAME = (By.ID, 'btnOutFrame')
    OF_FRAME = (By.CSS_SELECTOR, "div[id='link'] li:nth-child(1) a:nth-child(1)")
    FRAMES = (By.TAG_NAME,'iframe')



    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/iFrame")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_without_iFrame(self):
        self.driver.find_element(*self.WITHOUT_FRAME).click()
        alert = self.driver.switch_to.alert
        assert alert.text == 'Just Clicked Outside iFrame', "Should've gotten outside message"
        alert.accept()

    def test_of_iFrame(self):
        self.driver.switch_to.frame('myFrame1')
        self.driver.find_element(*self.OF_FRAME).click()
        print('I clicked in frame')
        time.sleep(3)
        print("Second window title = " + self.driver.title)

        try:
            self.driver.find_element(*self.OF_FRAME)
            print('Element exist')

        except NoSuchElementException:
            print("Element does not exist")

    def test_len_frames(self):
        frames = self.driver.find_elements(*self.FRAMES)
        for frame in frames:
            print(frame.get_attribute("id"))
        print(len(frames))



if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))