from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from PageObjects.base_page import BasePage
from config import RESET_PASSWORD_URL


class ResetPasswordPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.url = RESET_PASSWORD_URL
        self._password_field = (By.XPATH, "//input[@name='Введите новый пароль']")
        self._toggle_visibility_icon = (
        By.XPATH, "//input[@name='Введите новый пароль']/following-sibling::div[contains(@class, 'input__icon')]")

    def enter_password(self, password: str):
        el = self.wait_for_element_visible(self._password_field)
        el.clear()
        el.send_keys(password)
        return self

    def click_toggle_visibility(self):
        el = self.wait_for_element_clickable(self._toggle_visibility_icon)
        el.click()
        return self

    def get_password_field_type(self) -> str:
        el = self.wait_for_element_visible(self._password_field)
        return el.get_attribute("type")
