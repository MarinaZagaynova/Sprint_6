from selenium import webdriver

from pages.order_page import Order


class TestImportantQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_order(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        order = Order(self.driver)
        order.click_main_button_order()
        order.wait_text_order_page()
        order.check_open_page_order()
        order.click_logo_scooter()
        order.wait_text_main_page()
        order.check_open_main_page()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        order.wait_button_order_center()
        order.click_center_button_order()
        order.check_open_page_order()


