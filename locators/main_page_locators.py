from selenium.webdriver.common.by import By
from locators.base_locators import BUTTON

class MainPageLocators:
    # === Кнопки ===
    # Кнопка "Заказать" вверху страницы
    ORDER_BUTTON_TOP = (By.XPATH, BUTTON.format("Заказать"))
    
    # Кнопка "Заказать" внизу страницы
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    
    # === Логотипы ===
    # Логотип "Самокат"
    SCOOTER_LOGO = (By.XPATH, "//img[@src='/assets/scooter.svg']")
    
    # Логотип "Яндекс"
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    
    # === FAQ (Вопросы о важном) ===
    # Вопросы (по ID)
    QUESTION = (By.ID, "accordion__heading-{}")
    
    # Ответы (по ID)
    ANSWER = (By.ID, "accordion__panel-{}")