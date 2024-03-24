import pytest
from selenium import webdriver

from pages.important_questions_page import ImportantQuestionsPage
from pages.main_pages import MainPage
from pages.order_page import OrderPage


@pytest.fixture(scope='function')
def webpage():
    options = webdriver.FirefoxOptions()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox(options=options)
    url = 'https://qa-scooter.praktikum-services.ru/'
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(webpage):
    main_page = MainPage(webpage)
    return main_page


@pytest.fixture(scope='function')
def important_question_page(webpage):
    important_question_page = ImportantQuestionsPage(webpage)
    return important_question_page


@pytest.fixture(scope='function')
def order_page(webpage):
    order_page = OrderPage(webpage)
    return order_page
