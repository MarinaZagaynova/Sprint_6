from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.important_question_locators import ImportantQuestionsLocators


class ImportantQuestions:

    def __init__(self, driver):
        self.driver = driver

    def click_first_question(self):
        locators = ImportantQuestionsLocators
        self.driver.find_element(*locators.first_question).click()

    def get_first_answer(self):
        locators = ImportantQuestionsLocators
        return self.driver.find_element(*locators.first_answer).text

    def click_two_question(self):
        locators = ImportantQuestionsLocators
        self.driver.find_element(*locators.two_question).click()

    def get_two_answer(self):
        locators = ImportantQuestionsLocators
        return self.driver.find_element(*locators.two_answer).text

    def click_three_question(self):
        locators = ImportantQuestionsLocators
        self.driver.find_element(*locators.three_question).click()

    def get_three_answer(self):
        locators = ImportantQuestionsLocators
        return self.driver.find_element(*locators.three_answer).text

    def click_four_question(self):
        locators = ImportantQuestionsLocators
        self.driver.find_element(*locators.four_question).click()

    def get_four_answer(self):
        locators = ImportantQuestionsLocators
        return self.driver.find_element(*locators.four_answer).text

    def click_five_question(self):
        locators = ImportantQuestionsLocators
        self.driver.find_element(*locators.five_question).click()

    def get_five_answer(self):
        locators = ImportantQuestionsLocators
        return self.driver.find_element(*locators.five_answer).text

    def click_six_question(self):
        locators = ImportantQuestionsLocators
        self.driver.find_element(*locators.six_question).click()

    def get_six_answer(self):
        locators = ImportantQuestionsLocators
        return self.driver.find_element(*locators.six_answer).text

    def click_seven_question(self):
        locators = ImportantQuestionsLocators
        self.driver.find_element(*locators.seven_question).click()

    def get_seven_answer(self):
        locators = ImportantQuestionsLocators
        return self.driver.find_element(*locators.seven_answer).text

    def click_eight_question(self):
        locators = ImportantQuestionsLocators
        self.driver.find_element(*locators.eight_question).click()

    def get_eight_answer(self):
        locators = ImportantQuestionsLocators
        return self.driver.find_element(*locators.eight_answer).text

    def wait_first_answer(self):
        locators = ImportantQuestionsLocators
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.first_answer))

    def wait_two_answer(self):
        locators = ImportantQuestionsLocators
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.two_answer))

    def wait_three_answer(self):
        locators = ImportantQuestionsLocators
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.three_answer))

    def wait_four_answer(self):
        locators = ImportantQuestionsLocators
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.four_answer))

    def wait_five_answer(self):
        locators = ImportantQuestionsLocators
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.five_answer))

    def wait_six_answer(self):
        locators = ImportantQuestionsLocators
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.six_answer))

    def wait_seven_answer(self):
        locators = ImportantQuestionsLocators
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.seven_answer))

    def wait_eight_answer(self):
        locators = ImportantQuestionsLocators
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.eight_answer))
