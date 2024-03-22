from selenium.webdriver.common.by import By


class OrderLocators:
    button_main = [By.XPATH, "//div[@class='Header_Header__214zg']//button[@class='Button_Button__ra12g']"]
    button_center = [By.XPATH, "/div[@class='App_App__15LM-']//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']"]
    logo_scooter = [By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR"]
    logo_yandex = [By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI"]
    main_message = [By.CLASS_NAME, "Home_SubHeader__zwi_E"]
    text_order_page = [By.CLASS_NAME, "Order_Header__BZXOb"]


