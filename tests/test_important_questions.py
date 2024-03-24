import allure
import pytest

import data
from locators.important_question_locators import ImportantQuestionsLocators

class TestImportantQuestions:

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
    def test_first_question(self, num, result, important_question_page):
        important_question_page.scroll()
        assert important_question_page.get_answer_text(
            ImportantQuestionsLocators.QUESTION_LOCATORS,
            ImportantQuestionsLocators.ANSWER_LOCATORS,
            num
        ) == result
