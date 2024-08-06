from selenium.webdriver.common.by import By


class MainPageLocators:
    logo_yandex = [By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI"]
    yandex_locator = [By.XPATH, "//div[@class='desktop-base-header__logoContainer-3l desktop-base-header__isMorda-mX']"]
    QUESTION_LOCATORS = [By.ID, "accordion__heading-{}"]
    ANSWER_LOCATORS = [By.XPATH, ".//div[@id='accordion__panel-{}']/p"]
    main_message = [By.CLASS_NAME, "Home_SubHeader__zwi_E"]
    logo_scooter = [By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR"]


