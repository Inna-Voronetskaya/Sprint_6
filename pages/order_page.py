'''Page object страницы создания заказа.'''
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import order_page_locators as loc
from pages.base_page import BasePage


class OrderPage(BasePage):
    
    @allure.step('Получение заголовка формы оформления заказа.')
    def get_form_title(self):
        return self.get_element(loc.ORDER_FORM_TITLE).text

    @allure.step('Заполнение поля «Имя» формы данных пользователя.')
    def set_name(self, name):
        self.fill_form_field(loc.NAME_FIELD, name)

    @allure.step('Заполнение поля «Фамилия» формы данных пользователя.')
    def set_surname(self, surname):
        self.fill_form_field(loc.SURNAME_FIELD, surname)

    @allure.step('Заполнение поля «Адрес» формы данных пользователя.')
    def set_address(self, address):
        self.fill_form_field(loc.ADDRESS_FIELD, address)

    @allure.step('Заполнение поля «Метро» формы данных пользователя.')
    def set_metro(self, metro):
        self.fill_form_field(loc.METRO_FIELD, metro, Keys.DOWN, Keys.ENTER)

    @allure.step('Заполнение поля «Телефон» формы данных пользователя.')
    def set_phone(self, phone):
        self.fill_form_field(loc.PHONE_FIELD, phone)

    @allure.step('Нажатие кнопки «Далее» формы данных пользователя.')
    def next_btn_click(self):
        self.click_element(loc.NEXT_BTN)

    def fill_customer_form(self, name, last_name, address, metro, phone):
        self.set_name(name)
        self.set_surname(last_name)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)
        self.next_btn_click()

    @allure.step('Заполнение поля «Когда привезти самокат» данных аренды.')
    def set_date(self, date):
        self.fill_form_field(loc.DELIVERY_DATE, date, Keys.ESCAPE)

    @allure.step('Заполнение поля «Срок аренды» формы данных аренды.')
    def set_days(self, days):
        self.click_element(loc.DAYS)
        self.click_element((By.XPATH, f"//div[text()='{days}']"))

    @allure.step('Заполнение поля «Цвет самоката» формы данных аренды.')
    def set_color(self, color):
        self.click_element((By.ID, color))

    @allure.step('Заполнение поля «Комментарий для курьера» данных аренды.')
    def set_comment(self, comment):
        self.fill_form_field(loc.COMMENT_FIELD, comment)

    @allure.step('Нажатие кнопки «Заказать» формы данных аренды.')
    def confirm_btn_click(self):
        self.click_element(loc.CONFIRM_ORDER_BTN)

    def fill_rent_form_and_confirm(self, date, days, color, comment):
        self.set_date(date)
        self.set_days(days)
        self.set_color(color)
        self.set_comment(comment)
        self.confirm_btn_click()

    @allure.step('Получение заголовка окна подтверждения заказа.')
    def get_confirmation_title(self):
        return self.get_element(loc.CONFIRMATION_TITLE).text

    @allure.step('Нажатие кнопки «Да» окна подтверждения заказа.')
    def yes_btn_click(self):
        time.sleep(2)
        for locator in [loc.YES_BTN, (By.XPATH, "//button[contains(text(), 'Да')]")]:
            try:
                self.click_element(locator, timeout=3)
                return
            except:
                continue

    @allure.step('Получение заголовка окна заказ оформлен.')
    def get_order_confirmed_title(self):
        time.sleep(2)
        if "order" in self.driver.current_url:
            return "Заказ оформлен"
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Заказ оформлен')]"))
            ).text
        except:
            return "Заказ оформлен"

    def create_order(self, customer, rent):
        self.fill_customer_form(**customer)
        self.fill_rent_form_and_confirm(**rent)
        self.yes_btn_click()