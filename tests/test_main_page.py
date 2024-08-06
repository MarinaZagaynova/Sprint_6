import allure
import pytest

import data


class TestMainPage:

    @allure.title("Проверка редиректа в Яндекс")
    def test_yandex_redirect(self, main_page):
        main_page.click_logo_yandex()
        main_page.check_yandex_url()

    @allure.title("Проверка блока Важные вопросы")
    @pytest.mark.parametrize('num, result', [(0, data.answer_1),
                                             (1, data.answer_2),
                                             (2, data.answer_3),
                                             (3, data.answer_4),
                                             (4, data.answer_5),
                                             (5, data.answer_6),
                                             (6, data.answer_7),
                                             (7, data.answer_8)

                                             ])
    def test_questions(self, main_page, num, result):
        assert main_page.get_answer_text(num) == result

    @allure.title("Проверка перехода к главной странице по кнопке Логотипа")
    def test_logo_scooter(self, main_page, order_page):
        order_page.click_main_button_order()
        order_page.check_open_page_order()
        main_page.click_logo()
        main_page.check_open_main_page()
