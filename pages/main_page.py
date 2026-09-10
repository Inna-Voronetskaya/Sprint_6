from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MainPage(BasePage):
    
    def wait_for_load_main_page(self):
        self.wait_for_element(MainPageLocators.SCOOTER_LOGO)

    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)
        WebDriverWait(self.driver, 10).until(EC.url_contains("order"))

    def click_order_button_bottom(self):
        button = self.driver.find_element(*MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", button)
        WebDriverWait(self.driver, 10).until(EC.url_contains("order"))

    def order_button_click(self):
        self.click_order_button_bottom()

    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def click_question(self, index):
        locator = (By.ID, MainPageLocators.QUESTION[1].format(index))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element)

    def get_answer_text(self, index):
        locator = (By.ID, MainPageLocators.ANSWER[1].format(index))
        self.wait_for_element(locator)
        return self.get_text(locator)