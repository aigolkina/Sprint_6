import os
import sys
from selenium import webdriver
sys.path.append(os.path.join(os.getcwd(), ".."))
from pages.main_page import MainPage
from data_models.models import Models


class TestDropDownList:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

        cls.driver.get(Models.MAIN_URL)  # Зайти на сайт Заказа самокатов
        main_page = MainPage(cls.driver)
        main_page.tap_cookies_button()

    def test_dropdown_list_cost_of_scooters(self):
        main_page = MainPage(self.driver)

        main_page.tap_button_price()  # Найти меню-выпадашку "Сколько это стоит? И как оплатить?" и тапнуть на меню
        text = main_page.get_text_button_price()  # "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

        assert text == Models.TEXT_PRISE_BUTTON  # Проверка на выполнение тапа на меню

    def test_dropdown_list_quantity(self):
        main_page = MainPage(self.driver)

        main_page.tap_button_quantity()  # Найти меню-выпадашку "Хочу сразу несколько самокатов! Так можно?" и тапнуть на меню
        text = main_page.get_text_button_quantity()  # "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

        assert text == Models.TEXT_QUANTITY_BUTTON  # Проверка на выполнение тапа на меню

    def test_dropdown_list_rental_time(self):
        main_page = MainPage(self.driver)

        main_page.tap_button_time()  # Найти меню-выпадашку "Как рассчитывается время аренды?" и тапнуть на меню
        text = main_page.get_text_button_time()  # "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

        assert text == Models.TEXT_TIME_BUTTON  # Проверка на выполнение тапа на меню

    def test_dropdown_list_rental_scooter_for_today(self):
        main_page = MainPage(self.driver)

        main_page.tap_button_scooter_for_today()  # Найти меню-выпадашку "Можно ли заказать самокат прямо на сегодня?" и тапнуть на меню
        text = main_page.get_text_button_scooter_for_today()  # "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

        assert text == Models.TEXT_SCOOTER_FOR_TODAY_BUTTON  # Проверка на выполнение тапа на меню

    def test_dropdown_list_rental_order_extension(self):
        main_page = MainPage(self.driver)

        main_page.tap_button_order_extension()  # Найти меню-выпадашку "Можно ли продлить заказ или вернуть самокат раньше?" и тапнуть на меню
        text = main_page.get_text_button_order_extension()  # "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

        assert text == Models.TEXT_ORDER_EXTENSION_BUTTON  # Проверка на выполнение тапа на меню

    def test_dropdown_list_rental_charging(self):
        main_page = MainPage(self.driver)

        main_page.tap_button_charging()  # Найти меню-выпадашку "Вы привозите зарядку вместе с самокатом?" и тапнуть на меню
        text = main_page.get_text_button_charging()  # Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

        assert text == Models.TEXT_CHARGING_BUTTON  # Проверка на выполнение тапа на меню

    def test_dropdown_list_rental_order_cancellation(self):
        main_page = MainPage(self.driver)

        main_page.tap_button_order_cancellation()  # Найти меню-выпадашку "Можно ли отменить заказ?" и тапнуть на меню
        text = main_page.get_text_button_order_cancellation()  # "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

        assert text == Models.TEXT_ORDER_CANCELLATION_BUTTON  # Проверка на выполнение тапа на меню

    def test_dropdown_list_housing(self):
        main_page = MainPage(self.driver)

        main_page.tap_button_housing()  # Найти меню-выпадашку "Я жизу за МКАДом, привезёте?" и тапнуть на меню
        text = main_page.get_text_button_housing()  # "Да, обязательно. Всем самокатов! И Москве, и Московской области."

        assert text == Models.TEXT_HOUSING_BUTTON  # Проверка на выполнение тапа на меню

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()