from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from browser import Browser


class BasePage(Browser):

    def wait_and_click_elem_by_selector(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((by, selector)))
        self.driver.find_element(by, selector).click()

    def wait_and_fill_elem_by_selector(self, by, selector, text):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))
        self.driver.find_element(by, selector).send_keys(text)

    def verify_elem_is_displayed_by_selector(self, by, selector):
        elem = self.driver.find_element(by, selector)
        self.assertTrue(elem.is_displayed(), 'Elem not displayed')

    def verify_text_on_elem_by_selector(self, by, selector, expected_text):
        actual = self.driver.find_elements(by, selector).text
        self.assertEqual(expected_text, actual, 'Text on element is incorrect')

    def verify_page_url(self, expected_url):
        actual = self.driver.current_url
        self.assertEqual(expected_url, actual, 'URL is incorrect')