from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    RESULTS_TITLE = (By.XPATH, '//h2[@class="product-name"]')
    SELECT_XL_SIZE_BTN = (By.XPATH, '//*[contains(text(), " XL ")]')
    # ADAUGA_IN_COS_BTN = (By.XPATH, '//div[@class="row"]//button')
    ADAUGA_IN_COS_BTN = (By.XPATH, '//div[@class="row"]//button//span')
    # COSUL_MEU_BTN = (By.XPATH, '//div[@class="feature-icon-hover"]//child::a[2]//child::div')
    # COSUL_MEU_BTN = (By.ID, 'mini-cart')
    COSUL_MEU_BTN = (By.XPATH, '//button[@class="button btn-checkout btn-inline"]')
    COOKIES_BANNER = (By.CLASS_NAME, "cookiespopup-close")

    def verify_results_contains_text(self, text):
        title_list = self.driver.find_elements(*self.RESULTS_TITLE)
        for i in range(3):
            title = title_list[i].text.lower()
            self.assertTrue(text in title, 'Result does not contain search query')

    def select_product_by_name(self, name):
        self.driver.find_element(By.XPATH, f'//a[contains(text(), "{name}")]').click()

    def select_size(self, size):
        self.driver.find_element(By.XPATH, f'//div[contains(text(), " {size} ")]').click()

    def select_size_XL(self):
        self.wait_and_click_elem_by_selector(*self.SELECT_XL_SIZE_BTN)

    def add_product_to_basket(self):
        self.wait_and_click_elem_by_selector(*self.ADAUGA_IN_COS_BTN)

    def click_cart_btn(self):
        self.wait_and_click_elem_by_selector(*self.COSUL_MEU_BTN)

    def close_cookies_banner(self):
        self.wait_and_click_elem_by_selector(*self.COOKIES_BANNER)
