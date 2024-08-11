import os
import sys
import time

from helpers import Help

sys.path.append(os.path.join(os.getcwd(), ".."))
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data_models.models import Models
from selenium.webdriver.common.by import By


class OrderPage:

    __order_navbar_button = (By.CLASS_NAME, "Button_Button__ra12g")  # Кнопка "Заказать" в навбаре
    __order_button = (By.CLASS_NAME, "Button_Button__ra12g Button_Middle__1CSJM")  # Кнопка "Заказать" в блоке "Как это работает"
    __logo_scooter_button = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")  # Логотип "Самокат"
    __logo_yandex_button = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")  # Логотип "Яндекс"
    __name_input = (By.XPATH, "//input[@placeholder='* Имя']")  # Поле "Имя"
    __surname_input = (By.XPATH, "//input[@placeholder='* Фамилия']")  # Поле "Фамилия"
    __address_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # Поле "Адрес"
    __metro_station_input = (By.XPATH, "//input[@placeholder='* Станция метро']")  # Поле "Станция метро"
    __falcon_station_button = (By.CLASS_NAME, "Order_Text__2broi")  # Выбрать станцию "Сокол" в выпадающем списке
    __telephone_input = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # Поле "Телефон"
    __further_button = (By.XPATH, "//*[@id=\"root\"]/div/div[2]/div[3]/button")  # Кнопка "Далее"
    __date_input = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # Поле "Когда привезти самокат"
    __date_button = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--019 react-datepicker__day--selected react-datepicker__day--weekend'][text()='19']")  # Датапикер "Когда привезти заказ"
    __rental_period_input = (By.CLASS_NAME, "Dropdown-root")  # Поле "Срок аренды"
    __rental_period_button = (By.XPATH, "//div[@class='Dropdown-option'][text()='двое суток']")  # Срок аренды "двое суток"
    __color_checkbox = (By.ID, "black")  # Поле "Цвет самоката"
    __a_comment_input = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")  # Поле "Комментарий для курьера"
    __order_in_the_order_form_button = (By.XPATH, "//*[@id=\"root\"]/div/div[2]/div[3]/button[2]")  # Кнопка "Заказать"
    __yes_button = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][text()='Да']")  # Кнопка "Да" на поп-ап'е
    __order_completed_form = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][text()='Посмотреть статус']")  # Всплывающее окно с сообщением об успешном создании заказа

    def __init__(self, driver):
        self.driver = driver

    def tap_order_navbar(self):
        element_order_navbar = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__order_navbar_button))
        element_order_navbar.click()  # Найти кнопку "Заказать" в навбаре и тапнуть на нее

    def tap_name_input(self):
        element_name = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__name_input))
        element_name.click()  # Найти поле "Имя" и тапнуть на него
        element_name.send_keys("Анастасия")  # Ввести данные

    def tap_surname_input(self):
        element_surname = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__surname_input))
        element_surname.click()  # Найти поле "Фамилия" и ввести данные
        element_surname.send_keys("Иголкина")  # Ввести данные

    def tap_address_input(self):
        element_address = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__address_input))
        element_address.click()  # Найти поле "Адрес" и ввести данные
        element_address.send_keys("Ленинградский проспект, д.70")  # Ввести данные

    def tap_metro_station(self):
        element_metro_station = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__metro_station_input))
        element_metro_station.click()  # Найти поле "Станция метро" и ввести данные
        element_metro_station.send_keys("Сокол")  # Ввести данные

    def tap_falcon_station_input(self):
        element_metro_falcon_station = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__falcon_station_button))
        element_metro_falcon_station.click()  # Найти поле "Сокол" в меню выпадашке и тапнуть на него

    def tap_telephone_input(self):
        element_telephone = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__telephone_input))
        element_telephone.send_keys(Help.random_telephone())  # Найти поле "Телефон" и ввести данные

    def tap_further_button(self):
        element_further = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__further_button))
        element_further.click()  # Найти кнопку "Далее" и тапнуть на нее

    def tap_date_input(self):
        element_date = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__date_input))
        element_date.click()  # Найти поле "Дата" и тапнуть на него
        element_date.send_keys("19.10.2024")  # Ввести данные

    def tap_date_button(self):
        element_date_button= WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__date_button))
        element_date_button.click()  # Найти дату в датапикере и тапнуть на нее

    def tap_rental_period_input(self):
        element_rental_period_input = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__rental_period_input))
        element_rental_period_input.click()  # Найти поле "Когда привезти самокат?" и тапнуть на него

    def tap_rental_period_button(self):
        element_rental_period_button = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__rental_period_button))
        element_rental_period_button.click()  # Меню выпадашка со сроком аренды на двое суток

    def tap_color_checkbox(self):
        element_color = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__color_checkbox))
        element_color.click()  # Меню с выбором цвета самоката

    def tap_a_comment_input(self):
        element_a_comment = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__a_comment_input))
        element_a_comment.send_keys("Позвонить за час")  # Поле комментария для курьера

    def tap_order_in_the_order_form_button(self):
        element_a_comment = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__order_in_the_order_form_button))
        element_a_comment.click()  # Найти кнопку "Заказать" и тапнуть на нее

    def tap_yes_button(self):
        element_a_comment = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__yes_button))
        element_a_comment.click()  # Найти кнопку "Да" и тапнуть на нее

    def tap_order_completed_form(self):
        element_order_completed = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(self.__order_completed_form))
        assert element_order_completed.text == Models.ORDER_COMPLETED_FORM  # Проверка на выполнение оформления заказа

    def tap_logo_scooter_button(self):
        element_logo_scooter = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__logo_scooter_button))
        element_logo_scooter.click()  # Переход по лого "Самокат"

    # def tap_logo_yandex_button(self):
    #     element_logo_yandex = WebDriverWait(self.driver, Models.WAIT_TIME).until(
    #         expected_conditions.element_to_be_clickable(self.__logo_scooter_button))
    #     element_logo_yandex.click()  # Найти лого "Яндекс" в навбаре и тапнуть на него

    # def tap
    #     time.sleep(3)
    #     driver.switch_to.window(self.driver.window_handles[1])
    #     assert driver.current_url == "https://dzen.ru/?yredirect=true"  # Проверка перехода в Дзен