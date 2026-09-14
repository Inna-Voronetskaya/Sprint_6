import allure
import pytest

from pages.main_page import MainPage
from data import FAQ


class TestFAQ:
    @allure.title('Ответ на вопрос соответствует ожидаемому')
    @pytest.mark.parametrize("question_index", FAQ.keys())
    def test_faq_answers(self, driver, question_index):
        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.click_question(int(question_index))
        actual_answer = main_page.get_answer_text(int(question_index))
        assert actual_answer == FAQ.get_answer(question_index)