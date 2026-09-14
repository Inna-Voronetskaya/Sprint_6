from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def wait_for_load_main_page(self):
        self.wait_for_element(MainPageLocators.SCOOTER_LOGO)

    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)
        self.wait_for_url_contains("order")

    def click_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.js_click(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.wait_for_url_contains("order")

    def order_button_click(self):
        self.click_order_button_bottom()

    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def click_question(self, index):
        locator = (MainPageLocators.QUESTION[0], MainPageLocators.QUESTION[1].format(index))
        self.scroll_to_element(locator)
        self.js_click(locator)

    def get_answer_text(self, index):
        locator = (MainPageLocators.ANSWER[0], MainPageLocators.ANSWER[1].format(index))
        return self.get_text(locator)