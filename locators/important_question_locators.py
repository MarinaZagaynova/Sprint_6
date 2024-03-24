from selenium.webdriver.common.by import By


class ImportantQuestionsLocators:
    QUESTION_LOCATORS = [By.ID, "accordion__heading-{}"]
    ANSWER_LOCATORS = [By.XPATH, ".//div[@id='accordion__panel-{}']/p"]