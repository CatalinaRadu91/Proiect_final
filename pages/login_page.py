from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//*[@id="email"]')
    PASSWORD_INPUT = (By.ID, "pass")
    INTRA_IN_CONT_BTN = (By.ID, "send2")
    INVALID_MAIL_OR_PASS_MSG = (By.XPATH, '//li[@class="error-msg"]//child::ul//child::li//child::span')
    EMPTY_PASS_MSG = (By.ID, "advice-required-entry-pass")
    URL = "https://www.zonia.ro/customer/account/login"

    # aici nu va mai functiona daca sterg linia 16 si decomentez linia 17?
    def navigate_to_page(self):
        self.driver.get('https://www.zonia.ro/customer/account/login')
        # self.driver.get(self.URL)

    def insert_username(self, email):
        self.wait_and_fill_elem_by_selector(*self.EMAIL_INPUT, email)

    def insert_password(self, password):
        self.wait_and_fill_elem_by_selector(*self.PASSWORD_INPUT, password)

    def click_intra_in_cont(self):
        self.wait_and_click_elem_by_selector(*self.INTRA_IN_CONT_BTN)

    def check_error_message(self, error_message):
        actual_error_message = self.driver.find_element(*self.INVALID_MAIL_OR_PASS_MSG).text
        assert error_message == actual_error_message, f"Message is invalid. Expected: {error_message}, actual: {actual_error_message}"

    # e ok daca fac o metoda noua? sau ma puteam folosi de cea de sus doar prin schimbarea constantei? CUM?
    def check_error_message_for_empty_field(self, error_message):
        actual_error_message = self.driver.find_element(*self.EMPTY_PASS_MSG).text
        assert error_message == actual_error_message, f"Message is invalid. Expected: {error_message}, actual: {actual_error_message}"

    def get_empty_pass_msg(self):
        return self.driver.find_element(*self.EMPTY_PASS_MSG).text
