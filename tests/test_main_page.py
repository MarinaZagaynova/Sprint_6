import allure


class TestMainPage:

    @allure.title("Проверка редиректа в Яндекс")
    def test_yandex_redirect(self, main_page):
        main_page.click_logo_yandex()
        main_page.check_yandex_url()

