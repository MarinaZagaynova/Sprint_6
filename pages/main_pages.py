import time

import allure

import data
from locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажимаем на кнопку логотипа Яндекса")
    def click_logo_yandex(self):
        locators = MainPageLocators
        self.driver.find_element(*locators.logo_yandex).click()

    @allure.step("Проверяем переход на страницу яндекса")
    def check_yandex_url(self):
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == data.expected_redirect_url
