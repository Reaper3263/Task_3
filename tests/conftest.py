import pytest as pytest
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait

from pages.forgot_password import ForgotPasswordPage
from pages.main_page import MainPage
from pages.orders_list_page import OrdersListPage
from pages.profile_page import ProfilePage
from pages.reset_password import ResetPasswordPage
from config import MAIN_URL
from test_files.test_data import test_email, test_password
from tests.pages.login_page import LoginPage


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def setup_browser(request):
    browser_name = request.param

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Неизвестный браузер: {browser_name}")

    if request.cls is not None:
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
