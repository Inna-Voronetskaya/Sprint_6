'''Локаторы для страницы создания заказа.'''
from selenium.webdriver.common.by import By
from locators.base_locators import BUTTON, INPUT_FIELD, TEXT_IN_DIV

# === Заголовок формы ===
ORDER_FORM_TITLE = (By.XPATH, "//div[text()='Для кого самокат']")

# === Шаг 1: "Для кого самокат" ===
NAME_FIELD = (By.XPATH, INPUT_FIELD.format('* Имя'))
SURNAME_FIELD = (By.XPATH, INPUT_FIELD.format('* Фамилия'))
ADDRESS_FIELD = (By.XPATH, INPUT_FIELD.format('* Адрес: куда привезти заказ'))
METRO_FIELD = (By.XPATH, INPUT_FIELD.format('* Станция метро'))
PHONE_FIELD = (By.XPATH, INPUT_FIELD.format('* Телефон: на него позвонит курьер'))
NEXT_BTN = (By.XPATH, BUTTON.format('Далее'))

# === Шаг 2: "Про аренду" ===
DELIVERY_DATE = (By.XPATH, INPUT_FIELD.format('* Когда привезти самокат'))
DAYS = (By.XPATH, "//div[text()='* Срок аренды']")
COMMENT_FIELD = (By.XPATH, INPUT_FIELD.format('Комментарий для курьера'))
CONFIRM_ORDER_BTN = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Middle')]")
# === Окно подтверждения ===
CONFIRMATION_TITLE = (By.XPATH, "//div[contains(text(), 'Хотите оформить')]")
YES_BTN = (By.XPATH, "//button[text()='Да' and contains(@class, 'Button_Middle')]")

# === Окно "ЗАКАЗ ОФОРМЛЕН" ===
ORDER_CONFIRMED_TITLE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")