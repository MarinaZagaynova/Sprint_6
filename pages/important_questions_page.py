import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ImportantQuestionsPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("форматруем локаторы")
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    @allure.step("Получаем ответ на вопрос")
    def get_answer_text(self, locator_q, locator_a, num):
        locator_q_formatted = self.format_locators(locator_q, num)
        locator_a_formatted = self.format_locators(locator_a, num)
        self.click_to_element(locator_q_formatted)
        self.wait_answer(locator_a_formatted)
        return self.get_text_to_element(locator_a_formatted)

    @allure.step("Нажимаем на элемент {locator}")
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    @allure.step("Получаем текст элемента {locator}")
    def get_text_to_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Ждем ответ элемента {locator}")
    def wait_answer(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step("Скролл вниз")
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
