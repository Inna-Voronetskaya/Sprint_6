import allure
from pages.header_page import HeaderPage
from data import Urls


class TestHeaderPage:
    @allure.title('Кнопка "Заказать" в хедере открывает страницу заказа')
    def test_order_button_redirects_to_order_page(self, driver):
        header_page = HeaderPage(driver)
        header_page.open_main_page()
        header_page.accept_cookies()
        header_page.order_button_click()
        assert header_page.get_current_url() == Urls.ORDER_PAGE

    @allure.title('Редирект на Дзен по клику на лого Яндекс')
    def test_yandex_logo_opens_dzen(self, driver):
        header_page = HeaderPage(driver)
        header_page.open_main_page()
        header_page.accept_cookies()
        header_page.yandex_logo_click()
        header_page.wait_for_number_of_windows(2)
        header_page.switch_to_new_window()
        header_page.wait.until(lambda driver: driver.current_url != 'about:blank')
        assert 'dzen.ru' in header_page.get_current_url() or 'ya.ru' in header_page.get_current_url()

    @allure.title('Редирект на главную по клику на лого Самокат')
    def test_samokat_logo_opens_main_page(self, driver):
        header_page = HeaderPage(driver)
        header_page.open_main_page()
        header_page.accept_cookies()
        header_page.scooter_logo_click()
        assert header_page.get_current_url() == Urls.BASE_URL