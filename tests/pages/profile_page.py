import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.profile_page import ProfilePageLocators
from pages.base_page import BasePage
from config import PROFILE_URL


class ProfilePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = PROFILE_URL

    @allure.step("Нажатие на 'Профиль'")
    def click_profile(self):
        self.click_element(ProfilePageLocators.PROFILE_LINK)

    @allure.step("Нажатие на 'История заказов'")
    def click_order_history(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Нажатие на 'Выйти'")
    def click_exit(self):
        self.click_element(ProfilePageLocators.EXIT_LINK)
