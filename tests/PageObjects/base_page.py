from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver: WebDriver, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def wait_for_url_to_contain(self, partial_url: str, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.url_contains(partial_url))
            return True
        except TimeoutException:
            return False

    def wait_for_url_to_be(self, full_url: str, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.url_to_be(full_url))
            return True
        except TimeoutException:
            return False

    def wait_for_element_visible(self, locator: tuple, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator: tuple, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def click_element(self, locator: tuple, timeout: int = 10):
        el = self.wait_for_element_clickable(locator, timeout)
        el.click()

    def is_element_visible(self, locator: tuple, timeout: int = 10) -> bool:
        try:
            return self.wait_for_element_visible(locator, timeout).is_displayed()
        except TimeoutException:
            return False

    def is_element_invisible(self, locator: tuple, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                expected_conditions.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    def drag_and_drop_element(self, source_locator: tuple, target_locator: tuple, timeout: int = 10):
        source = self.wait_for_element_visible(source_locator, timeout)
        target = self.wait_for_element_visible(target_locator, timeout)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    def wait_for_text_in_element(self, locator: tuple, text: str, timeout: int = 10) -> bool:
        try:
            return WebDriverWait(self.driver, timeout).until(
                expected_conditions.text_to_be_present_in_element(locator, text)
            )
        except TimeoutException:
            return False