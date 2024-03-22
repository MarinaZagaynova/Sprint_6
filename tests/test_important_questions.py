from selenium import webdriver
from pages.important_questions_page import ImportantQuestions


class TestImportantQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_first_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions = ImportantQuestions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.click_first_question()
        questions.wait_first_answer()
        assert questions.get_first_answer() == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    def test_two_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions = ImportantQuestions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.click_two_question()
        questions.wait_two_answer()
        assert questions.get_two_answer() == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    def test_three_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions = ImportantQuestions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.click_three_question()
        questions.wait_three_answer()
        assert questions.get_three_answer() == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    def test_four_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions = ImportantQuestions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.click_four_question()
        questions.wait_four_answer()
        assert questions.get_four_answer() == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    def test_five_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions = ImportantQuestions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.click_five_question()
        questions.wait_five_answer()
        assert questions.get_five_answer() == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    def test_six_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions = ImportantQuestions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.click_six_question()
        questions.wait_six_answer()
        assert questions.get_six_answer() == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    def test_seven_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions = ImportantQuestions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.click_seven_question()
        questions.wait_seven_answer()
        assert questions.get_seven_answer() == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    def test_eight_question(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        questions = ImportantQuestions(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        questions.click_eight_question()
        questions.wait_eight_answer()
        assert questions.get_eight_answer() == "Да, обязательно. Всем самокатов! И Москве, и Московской области."

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
