from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountPage(BasePage):
    CONTUL_MEU_BTN = (By.XPATH, '//span[contains(text(), "Contul meu")]')
    LOGOUT_BTN = (By.XPATH, '//a[contains(text(), "Logout")]')

    def verify_account_page(self, expected_page_url):
        self.verify_page_url(expected_page_url)

    def click_contul_meu_btn(self):
        self.wait_and_click_elem_by_selector(*self.CONTUL_MEU_BTN)

    def click_logout_btn(self):
        self.wait_and_click_elem_by_selector(*self.LOGOUT_BTN)
