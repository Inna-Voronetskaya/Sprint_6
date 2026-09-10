import allure
import pytest

from data import BOOKED, CONFIRM_ORDER, RENT, SCOOTER_FOR, TestData
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


SCENARIO_1 = (HeaderPage, TestData.CUSTOMER_1, TestData.RENT_1)
SCENARIO_2 = (MainPage, TestData.CUSTOMER_2, TestData.RENT_2)


class TestOrderPage:
    @allure.title('Создание заказа')
    @pytest.mark.parametrize(
        'scenario',
        [pytest.param(SCENARIO_1, id='Header button'),
         pytest.param(SCENARIO_2, id='Main button')]
    )
    def test_create_order_with_button_header_or_main(self, driver, scenario):
        '''Создание заказа с использованием кнопки «Заказать» в хэдере
        и на главной странице.'''
        page_obj, customer, rent = scenario
        page_obj(driver).order_button_click()
        order_page = OrderPage(driver)
        
        # ✅ Ассерты перенесены в тест
        assert order_page.get_form_title() == SCOOTER_FOR
        
        order_page.create_order(customer, rent)
        
        assert BOOKED in order_page.get_order_confirmed_title()