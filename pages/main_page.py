import os
import sys
sys.path.append(os.path.join(os.getcwd(), ".."))
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data_models.models import Models
from selenium.webdriver.common.by import By


class MainPage:
    __cookies_button = (By.ID, "rcc-confirm-button")  # Куки
    __price_button = (By.ID, "accordion__heading-0")  # Кнопка "Сколько это стоит? И как оплатить?"
    __text_price_button = (By.XPATH, ".//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")  # Дискрипшн "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    __quantity_button = (By.ID, "accordion__heading-1")  # Кнопка "Хочу сразу несколько самокатов! Так можно?"
    __text_quantity_button = (By.XPATH, ".//p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")  # Дискрипшн "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    __time_button = (By.ID, "accordion__heading-2")  # Кнопка "Как рассчитывается время аренды?"
    __text_time_button = (By.XPATH, ".//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")  # Дискрипшн "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    __scooter_for_today_button = (By.ID, "accordion__heading-3")  # Кнопка "Можно ли заказать самокат прямо на сегодня?"
    __text_scooter_for_today_button = (By.XPATH, ".//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")  # Дискрипшн "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    __order_extension_button = (By.ID, "accordion__heading-4")  # Кнопка "Можно ли продлить заказ или вернуть самокат раньше?"
    __text_order_extension_button = (By.XPATH, ".//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")  # Дискрипшн "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    __charging_button = (By.ID, "accordion__heading-5")  # Кнопка "Вы привозите зарядку вместе с самокатом?"
    __text_charging_button = (By.XPATH, ".//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']")  # Дискрипшн "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    __order_cancellation_button = (By.ID, "accordion__heading-6")  # Кнопка "Можно ли отменить заказ?"
    __text_order_cancellation_button = (By.XPATH, ".//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")  # Дискрипшн "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    __housing_button = (By.ID, "accordion__heading-7")  # Кнопка "Я жизу за МКАДом, привезёте?"
    __text_housing_button = (By.XPATH, ".//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']")  # Дискрипшн "Да, обязательно. Всем самокатов! И Москве, и Московской области."


    def __init__(self, driver):
        self.driver = driver

    def tap_cookies_button(self):
        element_cookies = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__cookies_button))
        element_cookies.click()

    def tap_button_price(self):
        element_dropdown_menu_price = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__price_button))
        self.driver.execute_script('arguments[0].click()', element_dropdown_menu_price)

    def get_text_button_price(self):
        return WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(self.__text_price_button)).text

    def tap_button_quantity(self):
        element_dropdown_menu_quantity = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__quantity_button))
        self.driver.execute_script('arguments[0].click()', element_dropdown_menu_quantity)

    def get_text_button_quantity(self):
        return WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(self.__text_quantity_button)).text

    def tap_button_time(self):
        element_dropdown_menu_time = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__time_button))
        self.driver.execute_script('arguments[0].click()', element_dropdown_menu_time)

    def get_text_button_time(self):
        return WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(self.__text_time_button)).text


    def tap_button_scooter_for_today(self):
        element_dropdown_menu_scooter_for_today = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__scooter_for_today_button))
        self.driver.execute_script('arguments[0].click()', element_dropdown_menu_scooter_for_today)

    def get_text_button_scooter_for_today(self):
        return WebDriverWait(self.driver, Models.WAIT_TIME).until(
        expected_conditions.visibility_of_element_located(self.__text_scooter_for_today_button)).text

    def tap_button_order_extension(self):
        element_dropdown_menu_order_extension = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__order_extension_button))
        self.driver.execute_script('arguments[0].click()', element_dropdown_menu_order_extension)

    def get_text_button_order_extension(self):
        return WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(self.__text_order_extension_button)).text

    def tap_button_charging(self):
        element_dropdown_menu_charging = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__charging_button))
        self.driver.execute_script('arguments[0].click()', element_dropdown_menu_charging)

    def get_text_button_charging(self):
        return WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(self.__text_charging_button)).text

    def tap_button_order_cancellation(self):
        element_dropdown_menu_order_cancellation = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__order_cancellation_button))
        self.driver.execute_script('arguments[0].click()', element_dropdown_menu_order_cancellation)

    def get_text_button_order_cancellation(self):
        return WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(self.__text_order_cancellation_button)).text

    def tap_button_housing(self):
        element_dropdown_menu_housing = WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(self.__housing_button))
        self.driver.execute_script('arguments[0].click()', element_dropdown_menu_housing)

    def get_text_button_housing(self):
        return WebDriverWait(self.driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(self.__text_housing_button)).text