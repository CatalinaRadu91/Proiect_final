from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    TOTAL_PRICE = (By.CLASS_NAME, "price-int")
    REMOVE_BTN = (By.XPATH, '//td[@class="total-price-td"]//following::td//child::a')
    EMPTY_CART_MSG = (By.XPATH, '//div[@class="page-title"]//child::h1')

    def verify_total_price(self, expected_price):
        actual = self.driver.find_element(*self.TOTAL_PRICE).text
        self.assertEqual(actual, expected_price, "Price is incorrect")

    def click_remove_btn(self):
        self.wait_and_click_elem_by_selector(*self.REMOVE_BTN)

    def verify_empty_cart_msg(self):
        self.verify_elem_is_displayed_by_selector(*self.EMPTY_CART_MSG)
