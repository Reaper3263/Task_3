from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from PageObjects.base_page import BasePage
from config import FORGOT_PASSWORD_URL


class ForgotPasswordPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.url = FORGOT_PASSWORD_URL
        self._email_field = (By.XPATH, "//div[contains(@class, 'input')][./label[text()='Email']]/input")
        self._recover_button = (By.XPATH, "//button[text()='Восстановить']")

    def enter_email(self, email: str):
        el = self.wait_for_element_visible(self._email_field)
        el.clear()

        el.send_keys(email)

    def click_recover_btn(self):
        btn = self.wait_for_element_clickable(self._recover_button)
        btn.click()
