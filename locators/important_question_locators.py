from selenium.webdriver.common.by import By


class ImportantQuestionsLocators:
    first_question = [By.ID, "accordion__heading-0"]
    two_question = [By.ID, "accordion__heading-1"]
    three_question = [By.ID, "accordion__heading-2"]
    four_question = [By.ID, "accordion__heading-3"]
    five_question = [By.ID, "accordion__heading-4"]
    six_question = [By.ID, "accordion__heading-5"]
    seven_question = [By.ID, "accordion__heading-6"]
    eight_question = [By.ID, "accordion__heading-7"]
    first_answer = [By.XPATH, ".//div[@id='accordion__panel-0']/p"]
    two_answer = [By.XPATH, ".//div[@id='accordion__panel-1']/p"]
    three_answer = [By.XPATH, ".//div[@id='accordion__panel-2']/p"]
    four_answer = [By.XPATH, ".//div[@id='accordion__panel-3']/p"]
    five_answer = [By.XPATH, ".//div[@id='accordion__panel-4']/p"]
    six_answer = [By.XPATH, ".//div[@id='accordion__panel-5']/p"]
    seven_answer = [By.XPATH, ".//div[@id='accordion__panel-6']/p"]
    eight_answer = [By.XPATH, ".//div[@id='accordion__panel-7']/p"]