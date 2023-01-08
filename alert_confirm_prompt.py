
import unittest
import HTMLTestRunner
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Alerts(unittest.TestCase):
    HTML_ALERT = (By.CSS_SELECTOR, "#bootStrapAlertExample button")
    HTML_ALERT_TEXT = (By.ID, "bootStrapAlert")
    HTML_ALERT_CLOSE = (By.CSS_SELECTOR, '.btn-close')
    JS_ALERT = (By.CSS_SELECTOR, "#jsAlertExample button")
    JS_CONFIRM = (By.CSS_SELECTOR, "#jsConfirmExample button")
    RS_CONFIRM = (By.ID, "userResponse1")
    JS_PROMPT = (By.CSS_SELECTOR, "#jsPromptExample button")
    RS_PROMPT = (By.ID, 'userResponse2')
    INSERTED_TEXT = "test"

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/alert_confirm_prompt")
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_html_alert(self):
        self.driver.find_element(*self.HTML_ALERT).click()
        html_alert_text = self.driver.find_element(*self.HTML_ALERT_TEXT).text
        expected_text = "This is alert using just html."
        assert html_alert_text == expected_text, f"Error: expected: {expected_text}, actual: {html_alert_text}"
        self.driver.find_element(*self.HTML_ALERT_CLOSE).click()

        try:
            self.driver.find_element(*self.HTML_ALERT_CLOSE)
            print("Element still exist")

        except NoSuchElementException:
            print("Element does not exist, closed successfully")

    def test_js_alert_accept(self):
        self.driver.find_element(*self.JS_ALERT).click()
        js_alert = self.driver.switch_to.alert
        js_alert.accept()


    def test_js_confirm_accept_alert(self):
        self.driver.find_element(*self.JS_CONFIRM).click()
        js_confirm = self.driver.switch_to.alert
        js_confirm.accept()
        rs_message = self.driver.find_element(*self.RS_CONFIRM).text
        assert rs_message == 'Great! You will love it!', "Wrong message after accepting"

    def test_js_confirm_cancel_alert(self):
        self.driver.find_element(*self.JS_CONFIRM).click()
        js_confirm = self.driver.switch_to.alert
        js_confirm.dismiss()
        rs_message = self.driver.find_element(By.ID, *self.RS_CONFIRM).text
        assert rs_message == "Too bad!!! You would've loved it!", "Wrong message after canceling"

    def test_js_prompt_accept_alert_with_text(self):
        self.driver.find_element(*self.JS_PROMPT).click()
        js_prompt = self.driver.switch_to.alert
        js_prompt.send_keys(self.INSERTED_TEXT)
        js_prompt.accept()
        rs_message = self.driver.find_element(*self.RS_PROMPT).text
        expected_text = f"You have entered: {self.INSERTED_TEXT}"
        assert rs_message == expected_text, f"Error: expected: {expected_text}, actual: {rs_message}"

    def test_js_prompt_accept_alert_without_text(self):
        self.driver.find_element(*self.JS_PROMPT).click()
        js_prompt = self.driver.switch_to.alert
        js_prompt.accept()
        rs_message = self.driver.find_element(*self.RS_PROMPT).text
        expected_text = f"You have entered: none"
        assert rs_message == expected_text, f"Error: expected: {expected_text}, actual: {rs_message}"


if __name__ == '__main__' :
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='D:/selenium project/framework/reports'))
