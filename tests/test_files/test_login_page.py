import allure
import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.forgot_password import ForgotPasswordPage
from pages.reset_password import ResetPasswordPage
from tests.config import *


@pytest.mark.usefixtures("setup_pages")
class TestLoginPage:
    login_page: LoginPage
    forgot_pass_page: ForgotPasswordPage
    reset_pass_page: ResetPasswordPage
    driver: webdriver.Chrome

    @allure.title("Проверка открытия Восстановления пароля")
    def test_btn_forgot_password(self):
        self.login_page.open()
        self.login_page.click_forgot_password()

        assert self.login_page.wait_for_url_to_be(FORGOT_PASSWORD_URL)

    @allure.title("Проверка Восстановления пароля")
    def test_enter_email_and_click_recover(self):
        self.login_page.open()
        self.login_page.click_forgot_password()

        self.forgot_pass_page.enter_email("test@mail.ru")
        self.forgot_pass_page.click_recover_btn()

        assert self.login_page.wait_for_url_to_be(RESET_PASSWORD_URL)

    @allure.title("Проверка показа пароля")
    def test_show_hide_password(self):
        self.login_page.open()
        self.login_page.click_forgot_password()

        self.forgot_pass_page.enter_email("test@mail.ru")
        self.forgot_pass_page.click_recover_btn()

        self.reset_pass_page.enter_password("Secret123!")
        self.reset_pass_page.click_toggle_visibility()
        assert self.reset_pass_page.get_password_field_type() == "text"
