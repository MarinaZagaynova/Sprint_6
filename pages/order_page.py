import allure

import data
from locators.order_locators import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Скроллим страницу до кнопки заказать")
    def scrool_subheader(self):
        self.scroll_to_element(OrderLocators.BUTTON_CENTER)

    @allure.step("Нажимаем на кнопку 'Заказать' в верху страницы")
    def click_main_button_order(self):
        self.click_to_element(OrderLocators.button_main)

    @allure.step("Нажимаем на кнопку 'Заказать' в центре страницы")
    def click_element_order(self):
        self.click_to_element(OrderLocators.BUTTON_CENTER)

    @allure.step("Проверяем, что открыта страница заказа")
    def check_open_page_order(self):
        assert self.get_text_from_element(OrderLocators.text_order_page) == "Для кого самокат"

    @allure.step("Нажимаем на кнопку 'Самокат'")
    def click_logo_scooter(self):
        locators = OrderLocators
        self.driver.find_element(*locators.logo_scooter).click()

    @allure.step("Вводим имя")
    def set_name(self, name):
        self.send_text_to_element(OrderLocators.field_name, name)

    @allure.step("Вводим фамилию")
    def set_family_name(self, family_name):
        self.send_text_to_element(OrderLocators.field_family_name, family_name)

    @allure.step("Вводим адрес")
    def set_address(self, address):
        self.send_text_to_element(OrderLocators.field_address, address)

    @allure.step("Вводим метро")
    def set_metro(self, metro):
        self.send_text_to_element(OrderLocators.field_metro, metro)
        self.click_to_element(OrderLocators.station_list)

    @allure.step("Вводим телефон")
    def set_phone(self, phone):
        self.send_text_to_element(OrderLocators.field_phone, phone)

    @allure.step("Нажимаем на кнопку 'Далее'")
    def click_next(self):
        self.click_to_element(OrderLocators.button_next)

    @allure.step("Вводим дату доставки")
    def set_when(self):
        self.send_text_to_element(OrderLocators.field_when, data.when)
        self.click_to_element(OrderLocators.day_text)

    @allure.step("Вводим срок аренды")
    def set_term(self):
        self.click_to_element(OrderLocators.field_term)
        self.click_to_element(OrderLocators.rental_time)

    @allure.step("Вводим цвет")
    def set_color(self):
        self.click_to_element(OrderLocators.field_color)

    @allure.step("Вводим комментарий")
    def set_comment(self, comment):
        self.send_text_to_element(OrderLocators.field_comment, comment)

    @allure.step("Нажимаем на кнопку Да")
    def click_yes(self):
        self.click_to_element(OrderLocators.button_ok)

    @allure.step("Оформляем заказ")
    def click_order(self):
        self.click_to_element(OrderLocators.button_order)

    @allure.step("Проверяем, что заказ оформился")
    def check_order(self):
        assert self.get_text_from_element(OrderLocators.modal_message) == data.text_success_order

