from pages.base_page import BasePage


class AccountPage(BasePage):
    def verify_account_page(self,expected_page_url):
        self.verify_page_url(expected_page_url)
