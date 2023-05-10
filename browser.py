import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser(unittest.TestCase):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.set_page_load_timeout(200)

    def close(self):
        self.driver.delete_all_cookies()
        self.driver.close()
