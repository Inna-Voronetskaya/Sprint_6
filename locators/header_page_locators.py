from selenium.webdriver.common.by import By
from locators.base_locators import BUTTON

class HeaderPageLocators:
    ORDER_BTN = (By.XPATH, BUTTON.format("Заказать"))
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    SAMOKAT_LOGO = (By.XPATH, "//img[@src='/assets/scooter.svg']")
    COOKIE_BTN = (By.ID, "rcc-confirm-button")