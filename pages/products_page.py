from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    RESULTS_TITLE = (By.XPATH, '//h2[@class="product-name"]')
    # SELECT_SIZE_BTN = (By.CLASS_NAME, "attr-values-item")
    SELECT_S_SIZE_BTN = (By.XPATH, '//*[@id="attr-size-options-holder"]/div[1]')
    ADAUGA_IN_COS_BTN = (By.XPATH, '//div[@class="row"]//button')
    COSUL_MEU_BTN = (By.XPATH, '//div[@class="feature-icon-hover"]//child::a[2]//child::div')

    def verify_results_contains_text(self, text):
        title_list = self.driver.find_element(*self.RESULTS_TITLE)
        for i in range(4):
            title = title_list[i].text.lower()
            self.assertTrue(text in title, 'Result does not contain search query')

    def select_product_by_name(self, name):
        self.driver.find_element(By.XPATH, f'//a[contains(text(), "{name}")]').click()

    def select_size_S(self):
        self.wait_and_click_elem_by_selector(*self.SELECT_S_SIZE_BTN)

    # pot sa fac o metoda pentru care utilizatorul sa selecteze orice marime vrea?
    # metoda de mai jos nu functioneaza - nici selectorul folosit
    # def select_size(self, size):
    #     self.driver.find_element(By.XPATH, f'//div[contains(text(), "{size}")]').click()

    def add_product_to_basket(self):
        self.wait_and_click_elem_by_selector(*self.ADAUGA_IN_COS_BTN)



    def click_cart_btn(self):
        self.wait_and_click_elem_by_selector(*self.COSUL_MEU_BTN)
