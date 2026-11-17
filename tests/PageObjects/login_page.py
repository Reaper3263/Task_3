from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.base_page import BasePage
from tests.config import LOGIN_URL


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = LOGIN_URL

        self._username_field = (By.XPATH, "//input[@name='name']")
        self._password_field = (By.XPATH, "//input[@name='Пароль']")
        self._login_btn = (By.XPATH, "//button[text()='Войти']")
        self._recover_password_link = (By.XPATH, "//a[contains(@class, 'Auth_link') and text()='Восстановить пароль']")

    def click_forgot_password(self):
        el = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self._recover_password_link)
        )
        el.click()

    def enter_username(self, username: str):
        el = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self._username_field)
        )
        el.clear()
        el.send_keys(username)

    def enter_password(self, password: str):
        el = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self._password_field)
        )
        el.clear()
        el.send_keys(password)

    def click_login_button(self):
        el = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self._login_btn)
        )
        el.click()

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
