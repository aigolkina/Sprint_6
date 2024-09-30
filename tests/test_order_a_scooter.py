import os
import sys
import time

from selenium import webdriver
sys.path.append(os.path.join(os.getcwd(), ".."))
from pages.order_page import OrderPage
from data_models.models import Models
import pytest


class TestOrder:
    driver = None
    addresses = [
        'Тверская улица, дом 13'
    ]
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(Models.MAIN_URL)  # Зайти на сайт Заказа самокатов

    @pytest.mark.parametrize('name', ['Анастасия'])
    @pytest.mark.parametrize('address', addresses)
    def test_dropdown_list_order_via_navbar(self, name, address):
        order_page = OrderPage(self.driver)

        order_page.tap_order_navbar()  # Найти кнопку "Заказать" в навбаре и тапнуть на нее
        order_page.tap_name_input(name)  # Найти поле "Имя" и тапнуть на него и ввести данные
        order_page.tap_surname_input()  # Найти поле "Фамилия" и ввести данные и ввести данные
        order_page.tap_address_input(address)  # Найти поле "Адрес" и ввести данные
        order_page.tap_metro_station()  # Найти поле "Станция метро" и ввести данные
        order_page.tap_falcon_station_input()  # Найти поле "Сокол" в меню выпадашке и тапнуть на него
        order_page.tap_telephone_input()  # Найти поле "Телефон" и ввести данные
        order_page.tap_further_button()  # Найти кнопку "Далее" и тапнуть на нее
        order_page.tap_date_input()  # Найти поле "Дата" и тапнуть на него
        order_page.tap_date_button()  # Найти дату в датапикере и тапнуть на нее
        order_page.tap_rental_period_input()  # Найти поле "Когда привезти самокат?" И тапнуть на него
        order_page.tap_rental_period_button()  # Меню выпадашка со сроком аренды на двое суток
        order_page.tap_color_checkbox()  # Меню с выбором цвета самоката
        order_page.tap_a_comment_input()  # Поле комментария для курьера и ввести комментарий
        order_page.tap_order_in_the_order_form_button()  # Найти кнопку "Заказать" и тапнуть на нее
        order_page.tap_yes_button()  # Найти кнопку "Да" и тапнуть на нее
        order_page.tap_order_completed_form()  # Проверка на выполнение оформления заказа
        order_page.tap_logo_scooter_button()  # Переход по лого "Самокат" в навбаре и тапнуть на него
        current_url = order_page.tap_logo_yandex_button()  # Найти лого "Яндекс" в навбаре и тапнуть на него

        assert current_url == "https://dzen.ru/?yredirect=true"  # Проверка перехода в Дзен

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()