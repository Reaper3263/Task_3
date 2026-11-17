import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from locators.reset_password import ResetPasswordLocators
from pages.base_page import BasePage
from config import RESET_PASSWORD_URL


class ResetPasswordPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.url = RESET_PASSWORD_URL

    @allure.step("Ввод пароля")
    def enter_password(self, password: str):
        el = self.wait_for_element_visible(ResetPasswordLocators.PASSWORD_FIELD)
        el.clear()
        el.send_keys(password)
        return self

    @allure.step("Переключение видимости пароля")
    def click_toggle_visibility(self):
        self.click_element(ResetPasswordLocators.TOGLE_VISIBILITY_ICON)

    @allure.step("Получение типа поля пароля для проверки видимости")
    def get_password_field_type(self) -> str:
        el = self.wait_for_element_visible(ResetPasswordLocators.PASSWORD_FIELD)
        return el.get_attribute("type")
