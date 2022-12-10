import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("https://popageorgianvictor.github.io/PUBLISHED-WEBPAGES/checkbox")

to_select_value = '21-40'
locator_by_value = f'input[name="age-group-checkbox"][value="{to_select_value}"]'
my_choice = driver.find_element(By.CSS_SELECTOR, locator_by_value)
my_choice.click()

assert my_choice.is_selected(), f"After clicking value {to_select_value} it is not selected."

