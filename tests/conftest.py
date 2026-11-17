import pytest as pytest
from selenium import webdriver

from PageObjects.forgot_password import ForgotPasswordPage
from PageObjects.main_page import MainPage
from PageObjects.orders_list_page import OrdersListPage
from PageObjects.profile_page import ProfilePage
from PageObjects.reset_password import ResetPasswordPage
from config import MAIN_URL
from test_files.test_data import test_email, test_password
from tests.PageObjects.login_page import LoginPage


@pytest.fixture(scope="function")
def setup_browser(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.get(MAIN_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def setup_pages(request, setup_browser):
    request.cls.login_page = LoginPage(setup_browser)
    request.cls.forgot_pass_page = ForgotPasswordPage(setup_browser)
    request.cls.reset_pass_page = ResetPasswordPage(setup_browser)
    request.cls.main_page = MainPage(setup_browser)
    request.cls.profile_page = ProfilePage(setup_browser)
    request.cls.orders_list = OrdersListPage(setup_browser)


@pytest.fixture(scope="function")
def login_in_lk(request, setup_pages):
    request.cls.main_page.open_lk()
    request.cls.login_page.login(test_email, test_password)
