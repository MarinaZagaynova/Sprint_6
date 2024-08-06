import allure

import data
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Нажимаем на кнопку логотипа Яндекса")
    def click_logo_yandex(self):
        locators = MainPageLocators
        self.driver.find_element(*locators.logo_yandex).click()

    @allure.step("Проверяем переход на страницу яндекса")
    def check_yandex_url(self):
        assert self.switch_to_page(MainPageLocators.yandex_locator) == data.expected_redirect_url

    @allure.step("Получаем ответ на вопрос")
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATORS, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATORS, num)
        self.scroll_to_element(locator_q_formatted)
        self.click_to_element(locator_q_formatted)
        self.wait(locator_a_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Переход на главную страницу по клику на логотип')
    def click_logo(self):
        self.click_to_element(MainPageLocators.logo_scooter)

    @allure.step("Проверяем открытие главной страницы")
    def check_open_main_page(self):
        string = self.get_text_from_element(MainPageLocators.main_message)
        str = string.split(" ")
        assert str[1] == "его"

