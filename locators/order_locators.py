import pytest
from selenium.webdriver.common.by import By


class OrderLocators:
    button_main = [By.XPATH, "//div[@class='Header_Header__214zg']//button[@class='Button_Button__ra12g']"]
    BUTTON_CENTER = [By.XPATH, "//*[contains(@class, 'Button_Middle')]"]
    logo_scooter = [By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR"]

    main_message = [By.CLASS_NAME, "Home_SubHeader__zwi_E"]
    text_order_page = [By.CLASS_NAME, "Order_Header__BZXOb"]
    field_name = [By.XPATH, ".//input[@placeholder='* Имя']"]
    field_family_name = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    field_address = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    field_metro = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    station_list = [By.XPATH, "//div[@class = 'select-search__select']"]
    field_phone = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    button_next = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    field_when = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    day_text = [By.XPATH, '//div[contains(text(), "25")]']
    field_term = [By.XPATH, "//div[contains(text(), '* Срок аренды')]"]
    rental_time = [By.XPATH, "//div[contains(text(), 'сутки')]"]
    field_color = [By.XPATH, ".//label[@for='black']"]
    field_comment = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
    button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    button_ok = [By.XPATH, "//button[contains(text(), 'Да')]"]
    modal_message = [By.XPATH, "//button[contains(text(), 'Посмотреть статус')]"]






