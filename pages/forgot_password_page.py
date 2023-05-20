from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ForgotPassword(BasePage):
    EMAIL_ADDRESS_INPUT = (By.ID, 'email_address')
    SEND_PASSWORD_BTN = (By.XPATH, '//button[@title="Send password"]')
    SUCCESS_RESET_PASS_MSG = (By.XPATH, '//li[@class="success-msg"]')
    ERROR_RESET_PASS_MSG = (By.XPATH, '//li[@class="error-msg"]')

    def verify_forgot_password_page(self, expected_page_url):
        self.verify_page_url(expected_page_url)

    def insert_email_address(self, email_address):
        self.wait_and_fill_elem_by_selector(*self.EMAIL_ADDRESS_INPUT, email_address)

    def click_send_password(self):
        self.wait_and_click_elem_by_selector(*self.SEND_PASSWORD_BTN)

    def check_success_msg(self, success_msg):
        actual_success_msg = self.driver.find_element(*self.SUCCESS_RESET_PASS_MSG).text
        assert success_msg == actual_success_msg, f"Invalid msg. Expected: {success_msg}, actual: {actual_success_msg}"

    def check_error_msg(self, error_msg):
        actual_error_msg = self.driver.find_element(*self.ERROR_RESET_PASS_MSG).text
        assert error_msg == actual_error_msg, f"Message is invalid. Expected: {error_msg}, actual: {actual_error_msg}"
