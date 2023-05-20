from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//*[@id="email"]')
    PASSWORD_INPUT = (By.ID, "pass")
    INTRA_IN_CONT_BTN = (By.ID, "send2")
    INVALID_MAIL_OR_PASS_MSG = (By.XPATH, '//li[@class="error-msg"]//child::ul//child::li//child::span')
    EMPTY_FIELD_MSG = (By.XPATH, '//div[contains(text(), "Camp obligatoriu")]')
    URL = "https://www.zonia.ro/customer/account/login"
    FORGOT_PASS_LINK = (By.XPATH, '//a[@class="f-left"]')

    def navigate_to_page(self):
        self.driver.get('https://www.zonia.ro/customer/account/login')
        # self.driver.get(self.URL)

    def verify_login_page(self, expected_page_url):
        self.verify_page_url(expected_page_url)

    def insert_username(self, email):
        self.wait_and_fill_elem_by_selector(*self.EMAIL_INPUT, email)

    def insert_password(self, password):
        self.wait_and_fill_elem_by_selector(*self.PASSWORD_INPUT, password)

    def click_intra_in_cont(self):
        self.wait_and_click_elem_by_selector(*self.INTRA_IN_CONT_BTN)

    def check_error_message(self, error_message):
        actual_error_message = self.driver.find_element(*self.INVALID_MAIL_OR_PASS_MSG).text
        assert error_message == actual_error_message, f"Message is invalid. Expected: {error_message}, actual: {actual_error_message}"

    def check_error_message_for_empty_field(self, error_message):
        actual_error_message = self.driver.find_element(*self.EMPTY_FIELD_MSG).text
        assert error_message == actual_error_message, f"Message is invalid. Expected: {error_message}, actual: {actual_error_message}"

    def click_forgot_pass_link(self):
        self.wait_and_click_elem_by_selector(*self.FORGOT_PASS_LINK)
