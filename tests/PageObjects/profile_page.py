from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.base_page import BasePage
from config import PROFILE_URL


class ProfilePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = PROFILE_URL

        self._profile_link = (By.XPATH, "//a[normalize-space()='Профиль']")
        self._order_history_link = (By.XPATH, "//a[normalize-space()='История заказов']")
        self._exit_link = (By.XPATH, "//button[text()='Выход']")

    def click_profile(self):
        el = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self._profile_link)
        )
        el.click()

    def click_order_history(self):
        el = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self._order_history_link)
        )
        el.click()

    def click_exit(self):
        el = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self._exit_link)
        )
        el.click()
