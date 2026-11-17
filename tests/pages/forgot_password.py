import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from locators.forgot_password import ForgotPasswordLocators
from pages.base_page import BasePage
from config import FORGOT_PASSWORD_URL


class ForgotPasswordPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.url = FORGOT_PASSWORD_URL

    @allure.step("Ввод email {email}")
    def enter_email(self, email: str):
        el = self.wait_for_element_visible(ForgotPasswordLocators.EMAIL_FIELD)
        el.clear()

        el.send_keys(email)

    @allure.step("Нажатие кнопки восстановить пароль")
    def click_recover_btn(self):
        btn = self.wait_for_element_clickable(ForgotPasswordLocators.RECOVER_BUTTON)
        btn.click()
