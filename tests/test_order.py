import allure
import pytest

from data import BOOKED, SCOOTER_FOR, TestData
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


SCENARIO_1 = (HeaderPage, TestData.CUSTOMER_1, TestData.RENT_1)
SCENARIO_2 = (MainPage, TestData.CUSTOMER_2, TestData.RENT_2)


class TestOrderPage:

    @allure.title('Проверка заголовка формы заказа')
    @pytest.mark.parametrize(
        'scenario',
        [pytest.param(SCENARIO_1, id='Header button'),
         pytest.param(SCENARIO_2, id='Main button')]
    )
    def test_form_title(self, driver, scenario):
        page_obj, customer, rent = scenario
        page_obj(driver).order_button_click()
        order_page = OrderPage(driver)
        assert order_page.get_form_title() == SCOOTER_FOR

    @allure.title('Создание заказа')
    @pytest.mark.parametrize(
        'scenario',
        [pytest.param(SCENARIO_1, id='Header button'),
         pytest.param(SCENARIO_2, id='Main button')]
    )
    def test_create_order(self, driver, scenario):
        page_obj, customer, rent = scenario
        page_obj(driver).order_button_click()
        order_page = OrderPage(driver)
        order_page.create_order(customer, rent)
        assert BOOKED in order_page.get_order_confirmed_title()