import os
import sys
from selenium import webdriver
sys.path.append(os.path.join(os.getcwd(), ".."))
from pages.order_page import OrderPage
from data_models.models import Models


class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(Models.MAIN_URL)  # Зайти на сайт Заказа самокатов

    def test_dropdown_list_order_via_navbar(self):
        order_page = OrderPage(self.driver)

        order_page.tap_order_navbar()
        order_page.tap_name_input()
        order_page.tap_surname_input()
        order_page.tap_address_input()
        order_page.tap_metro_station()
        order_page.tap_falcon_station_input()
        order_page.tap_telephone_input()
        order_page.tap_further_button()
        order_page.tap_date_input()
        order_page.tap_date_button()
        order_page.tap_rental_period_input()
        order_page.tap_rental_period_button()
        order_page.tap_color_checkbox()
        order_page.tap_a_comment_input()
        order_page.tap_order_in_the_order_form_button()
        order_page.tap_yes_button()
        order_page.tap_order_completed_form()
        # order_page.tap_logo_scooter_button()
        # order_page.tap_logo_yandex_button()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()