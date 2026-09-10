import pytest
from pages.main_page import MainPage

class TestFAQ:
    EXPECTED_ANSWERS = [
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
    ]

    @pytest.mark.parametrize("question_index, expected_answer", [
        (0, EXPECTED_ANSWERS[0]),
        (1, EXPECTED_ANSWERS[1]),
        (2, EXPECTED_ANSWERS[2]),
        (3, EXPECTED_ANSWERS[3]),
        (4, EXPECTED_ANSWERS[4]),
        (5, EXPECTED_ANSWERS[5]),
        (6, EXPECTED_ANSWERS[6]),
        (7, EXPECTED_ANSWERS[7]),
    ])
    def test_faq_answers(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.click_question(question_index)
        actual_answer = main_page.get_answer_text(question_index)
        assert actual_answer == expected_answer, (
            f"Ожидалось: {expected_answer}, получено: {actual_answer}"
        )