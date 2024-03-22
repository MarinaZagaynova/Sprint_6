from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_locators import OrderLocators


class Order:
    def __init__(self, driver):
        self.driver = driver

    def click_main_button_order(self):
        locators = OrderLocators
        self.driver.find_element(*locators.button_main).click()

    def click_center_button_order(self):
        locators = OrderLocators
        self.driver.find_element(*locators.button_center).click()

    def wait_text_order_page(self):
        locators = OrderLocators
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.text_order_page))

    def wait_text_main_page(self):
        locators = OrderLocators
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.main_message))

    def wait_button_order_center(self):
        locators = OrderLocators
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locators.button_center))

    def check_open_page_order(self):
        locators = OrderLocators
        assert self.driver.find_element(*locators.text_order_page).text == "Для кого самокат"

    def click_logo_scooter(self):
        locators = OrderLocators
        self.driver.find_element(*locators.logo_scooter).click()

    def click_logo_yandex(self):
        locators = OrderLocators
        self.driver.find_element(*locators.logo_yandex).click()

    def check_open_main_page(self):
        locators = OrderLocators
        string = self.driver.find_element(*locators.main_message).text
        str = string.split(" ")
        assert str[1] == "его"


