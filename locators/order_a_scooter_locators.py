import os
import sys
from selenium.webdriver.common.by import By
sys.path.append(os.path.join(os.getcwd(), ".."))


class OrderAScooterLocators:
    ORDER_NAVBAR_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")  # Кнопка "Заказать" в навбаре
    ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g Button_Middle__1CSJM")  # Кнопка "Заказать" в блоке "Как это работает"
    LOGO_SCOOTER_BUTTON = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")  # Логотип "Самокат"
    LOGO_YANDEX_BUTTON = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")  # Логотип "Яндекс"

    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")  # Поле "Имя"
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")  # Поле "Фамилия"
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # Поле "Адрес"
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")  # Поле "Станция метро"
    FALCON_STATION_BUTTON = (By.CLASS_NAME, "Order_Text__2broi")  # Выбрать станцию "Сокол" в выпадающем списке
    TELEPHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # Поле "Телефон"
    FURTHER_BUTTON = (By.XPATH, "//*[@id=\"root\"]/div/div[2]/div[3]/button")  # Кнопка "Далее"

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # Поле "Когда привезти самокат"
    DATE_BUTTON = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--019 react-datepicker__day--selected react-datepicker__day--weekend'][text()='19']")  # Датапикер "Когда привезти заказ"
    RENTAL_PERIOD_INPUT = (By.CLASS_NAME, "Dropdown-root")  # Поле "Срок аренды"
    RENTAL_PERIOD_BUTTON = (By.XPATH, "//div[@class='Dropdown-option'][text()='двое суток']")
    COLOR_CHECKBOX = (By.ID, "black")  # Поле "Цвет самоката"
    A_COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")  # Поле "Комментарий для курьера"
    ORDER_IN_THE_ORDER_FORM_BUTTON = (By.XPATH, "//*[@id=\"root\"]/div/div[2]/div[3]/button[2]")  # Кнопка "Заказать"
    YES_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][text()='Да']")  # Кнопка "Да" на поп-ап'е
    ORDER_COMPLETED_FORM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][text()='Посмотреть статус']")  # Всплывающее окно с сообщением об успешном создании заказа
