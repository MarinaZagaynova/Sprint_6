import time

import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
from locators.order_locators import OrderLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Скроллим страницу до кнопки заказать")
    def scrool_subheader(self):
        locators = OrderLocators
        element = self.driver.find_element(*locators.BUTTON_CENTER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Нажимаем на кнопку 'Заказать' в верху страницы")
    def click_main_button_order(self):
        locators = OrderLocators
        self.driver.find_element(*locators.button_main).click()

    @allure.step("Нажимаем на кнопку 'Заказать' в центре страницы")
    def click_element_order(self):
        locators = OrderLocators
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(OrderLocators.BUTTON_CENTER))
        self.driver.find_element(*locators.BUTTON_CENTER).click()

    @allure.step("Проверяем, что открыта страница заказа")
    def check_open_page_order(self):
        locators = OrderLocators
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.text_order_page))
        assert self.driver.find_element(*locators.text_order_page).text == "Для кого самокат"

    @allure.step("Нажимаем на кнопку 'Самокат'")
    def click_logo_scooter(self):
        locators = OrderLocators
        self.driver.find_element(*locators.logo_scooter).click()

    @allure.step("Проверяем открытие главной страницы")
    def check_open_main_page(self):
        locators = OrderLocators
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.main_message))
        string = self.driver.find_element(*locators.main_message).text
        str = string.split(" ")
        assert str[1] == "его"

    @allure.step("Вводим имя")
    def set_name(self, name):
        locators = OrderLocators
        self.driver.find_element(*locators.field_name).send_keys(name)

    @allure.step("Вводим фамилию")
    def set_family_name(self, family_name):
        locators = OrderLocators
        self.driver.find_element(*locators.field_family_name).send_keys(family_name)

    @allure.step("Вводим адрес")
    def set_address(self, family_name):
        locators = OrderLocators
        self.driver.find_element(*locators.field_address).send_keys(family_name)

    @allure.step("Вводим метро")
    def set_metro(self, metro):
        locators = OrderLocators
        self.driver.find_element(*locators.field_metro).send_keys(metro)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locators.station_list))
        self.driver.find_element(*locators.station_list).click()

    @allure.step("Вводим телефон")
    def set_phone(self, phone):
        locators = OrderLocators
        self.driver.find_element(*locators.field_phone).send_keys(phone)

    @allure.step("Нажимаем на кнопку 'Далее'")
    def click_next(self):
        locators = OrderLocators
        self.driver.find_element(*locators.button_next).click()

    @allure.step("Вводим дату доставки")
    def set_when(self):
        locators = OrderLocators
        self.driver.find_element(*locators.field_when).send_keys(data.when)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locators.day_text))
        self.driver.find_element(*locators.day_text).click()

    @allure.step("Вводим срок аренды")
    def set_term(self):
        locators = OrderLocators
        self.driver.find_element(*locators.field_term).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locators.rental_time))
        self.driver.find_element(*locators.rental_time).click()

    @allure.step("Вводим цвет")
    def set_color(self):
        locators = OrderLocators
        self.driver.find_element(*locators.field_color).click()

    @allure.step("Вводим комментарий")
    def set_comment(self, comment):
        locators = OrderLocators
        self.driver.find_element(*locators.field_comment).send_keys(comment)

    @allure.step("Нажимаем на кнопку Да")
    def click_yes(self):
        locators = OrderLocators
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locators.button_ok))
        self.driver.find_element(*locators.button_ok).click()

    @allure.step("Оформляем заказ")
    def click_order(self):
        locators = OrderLocators
        self.driver.find_element(*locators.button_order).click()

    @allure.step("Проверяем, что заказ оформился")
    def check_order(self):
        locators = OrderLocators
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locators.modal_message))
        assert self.driver.find_element(*locators.modal_message).text == 'Посмотреть статус'