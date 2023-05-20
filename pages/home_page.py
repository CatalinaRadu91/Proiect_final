from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class HomePage(BasePage):
    NOTIFICATION_BTN = (By.ID, "onesignal-slidedown-allow-button")
    CONTUL_MEU_BTN = (By.XPATH, '//*[@id="my-account-ddown"]')
    LOGIN_BTN = (By.XPATH, '//a[contains(text(), "Login")]')
    SEARCH_INPUT = (By.XPATH, '//input[@id="search"]')
    TAB_ITEM = (By.XPATH, f'//ul[@id="nav"]//span[contains(text(),"Placeholder")]/parent::a[@class="level-top"]')

    def click_on_menu_tab(self, tab_name):
        self.wait_and_click_elem_by_selector(self.TAB_ITEM[0],
                                             self.TAB_ITEM[1].replace("Placeholder", tab_name))

    def navigate_to_home_page(self):
        self.driver.get('https://www.zonia.ro/')

    def click_accept_notification_btn(self):
        self.wait_and_click_elem_by_selector(*self.NOTIFICATION_BTN)

    def click_contul_meu_btn(self):
        self.wait_and_click_elem_by_selector(*self.CONTUL_MEU_BTN)

    def click_login_btn(self):
        self.wait_and_click_elem_by_selector(*self.LOGIN_BTN)

    def search_after(self, query):
        self.wait_and_fill_elem_by_selector(*self.SEARCH_INPUT, query)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)
        sleep(5)

    def verify_home_page(self, expected_page_url):
        self.verify_page_url(expected_page_url)
