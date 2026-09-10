from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators
from data import Urls


class HeaderPage(BasePage):
    
    def open_main_page(self):
        self.driver.get(Urls.BASE_URL)

    def order_button_click(self):
        self.click_element(HeaderPageLocators.ORDER_BTN)

    def yandex_logo_click(self):
        self.click_element(HeaderPageLocators.YANDEX_LOGO)

    def scooter_logo_click(self):
        self.click_element(HeaderPageLocators.SAMOKAT_LOGO)

    def accept_cookies(self):
        try:
            self.click_element(HeaderPageLocators.COOKIE_BTN)
        except:
            pass