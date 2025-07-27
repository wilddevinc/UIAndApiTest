import allure
from selenium.webdriver.support.ui import WebDriverWait
from page import Page
from locators_login_page import Login
import time

class MainPage(Page, Login):

    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url
        self.wait = WebDriverWait(driver, 10)

    def step_input_login_data(self, login):
        with allure.step(f"Ввод логина: {login}"):
            self.find_element(self.LOGIN_INPUT).click()
            self.find_element(self.LOGIN_INPUT).clear()
            self.find_element(self.LOGIN_INPUT).send_keys(login)

    def step_input_pass_data(self, password):
        with allure.step("Ввод пароля"):
            self.find_element(self.PASS_INPUT).click()
            self.find_element(self.PASS_INPUT).clear()
            self.find_element(self.PASS_INPUT).send_keys(password)

    def authorize(self, login, password):
        with allure.step("Авторизация пользователя"):
            self.step_input_login_data(login)
            self.step_input_pass_data(password)

    def step_click_button_submit(self):
        with allure.step("Клик по кнопке Войти"):
            self.find_element(self.SUBMIT_BT).click()

    def step_click_devices_online(self):
        with allure.step("Открытие вкладки устройств онлайн"):
            self.find_element(self.DEVICES_ONLINE).click()

    def step_click_change_columns(self):
        with allure.step("Открытие меню изменения столбцов."):
            self.find_element(self.CHANGE_COLUMNS).click()

    def step_click_close_device_menu(self):
        with allure.step("Закрытие меню устройств"):
            self.is_element_visible(self.DEVICE_MENU_CLOSE)
            self.find_element(self.DEVICE_MENU_CLOSE).click()

    def step_download_report(self):
        with allure.step("Нажатие кнопки загрузки отчёта"):
            self.wait_element(self.DOWNLOAD_REPORT_BUTTON)
            self.find_element(self.DOWNLOAD_REPORT_BUTTON).click()

    def step_check_popup(self):
        with allure.step("Ожидание появления попапа успешной загрузки"):
            self.wait_element(self.SUCCESSFULY_DOWNLOAD_POPUP)

    def step_click_on_download_report_link(self):
        with allure.step("Клик по ссылке загрузки отчёта в попапе"):
            self.is_element_visible(self.DOWNLOAD_LINK)
            self.find_element(self.DOWNLOAD_LINK).click()

    def step_check_report_download_successful(self):
        with allure.step("Закрытие попапа успешной загрузки"):
            self.find_element(self.SUCCESSFULY_DOWNLOAD_POPUP).click()

    def step_ui_test(self):
        with allure.step("Выполнение UI теста: навигация и загрузка отчёта"):
            self.step_click_devices_online()
            self.step_click_change_columns()
            self.step_click_close_device_menu()
            self.step_download_report()
            self.step_check_popup()
            self.step_click_on_download_report_link()
