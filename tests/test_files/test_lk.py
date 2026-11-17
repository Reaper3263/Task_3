import allure
import pytest
from selenium import webdriver

from PageObjects.login_page import LoginPage
from PageObjects.main_page import MainPage
from PageObjects.profile_page import ProfilePage
from config import LOGIN_URL, ORDER_HISTORY_URL
from test_files.test_data import test_email, test_password


@pytest.mark.usefixtures("setup_pages")
class TestLK:
    driver: webdriver.Chrome
    main_page: MainPage
    login_page: LoginPage
    profile_page: ProfilePage

    @allure.title("Проверка открытия личного кабинета")
    def test_click_lk(self):
        self.main_page.open_lk()
        assert self.login_page.wait_for_url_to_be(LOGIN_URL)

    @allure.title("Проверка перехода а Историю заказов")
    def test_check_orders_history(self):
        self.main_page.open_lk()
        self.login_page.login(test_email, test_password)
        self.main_page.open_lk()
        self.profile_page.click_order_history()
        assert self.profile_page.wait_for_url_to_be(ORDER_HISTORY_URL)

    @allure.title("Проверка выхода из личного кабинета")
    def test_check_exit(self):
        self.main_page.open_lk()
        self.login_page.login(test_email, test_password)
        self.main_page.open_lk()
        self.profile_page.click_exit()
        assert self.profile_page.wait_for_url_to_be(LOGIN_URL)
