import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.login_page import LoginPageLocators
from pages.base_page import BasePage
from tests.config import LOGIN_URL


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver, url=LOGIN_URL)

    @allure.step("Нажать на 'Восстановить пароль'")
    def click_forgot_password(self):
        self.click_element(LoginPageLocators.RECOVER_PASSWORD_LINK)

    @allure.step("Ввести логин '{username}'")
    def enter_username(self, username: str):
        el = self.wait_for_element_visible(LoginPageLocators.USERNAME_FIELD)
        el.clear()
        el.send_keys(username)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str):
        el = self.wait_for_element_visible(LoginPageLocators.PASSWORD_FIELD)
        el.clear()
        el.send_keys(password)

    @allure.step("Нажать на кнопку Войти")
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BTN)

    @allure.step("Авторизоваться под пользователем '{username}'")
    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
