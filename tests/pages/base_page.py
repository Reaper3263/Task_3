import time

from selenium.common import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    IGNORED_EXCEPTIONS = (
        StaleElementReferenceException,
        ElementClickInterceptedException,
    )

    def __init__(self, driver: WebDriver, url=None):
        self.driver = driver
        self.url = url

    def _get_wait(self, timeout: int = 10, poll_frequency: float = 0.5) -> WebDriverWait:
        return WebDriverWait(
            self.driver,
            timeout=timeout,
            poll_frequency=poll_frequency,
            ignored_exceptions=self.IGNORED_EXCEPTIONS,
        )

    def open(self):
        self.driver.get(self.url)

    def wait_for_url_to_contain(self, partial_url: str, timeout: int = 10) -> bool:
        try:
            self._get_wait(timeout).until(expected_conditions.url_contains(partial_url))
            return True
        except TimeoutException:
            return False

    def wait_for_url_to_be(self, full_url: str, timeout: int = 10) -> bool:
        try:
            self._get_wait(timeout).until(expected_conditions.url_to_be(full_url))
            return True
        except TimeoutException:
            return False

    def wait_for_element_visible(self, locator: tuple, timeout: int = 10):
        return self._get_wait(timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator: tuple, timeout: int = 10):
        return self._get_wait(timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def click_element(self, locator: tuple, timeout: int = 10, retries: int = 3):
        last_exception = None
        for _ in range(retries):
            try:
                el = self.wait_for_element_clickable(locator, timeout)
                el.click()
                return
            except self.IGNORED_EXCEPTIONS as exc:
                last_exception = exc
                time.sleep(0.3)

        try:
            el = self.wait_for_element_visible(locator, timeout)
            self.driver.execute_script("arguments[0].click();", el)
        except Exception as exc:
            raise last_exception or exc

    def is_element_visible(self, locator: tuple, timeout: int = 10) -> bool:
        try:
            return self.wait_for_element_visible(locator, timeout).is_displayed()
        except TimeoutException:
            return False

    def is_element_invisible(self, locator: tuple, timeout: int = 10):
        try:
            return self._get_wait(timeout).until(
                expected_conditions.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    def drag_and_drop_element(self, source_locator: tuple, target_locator: tuple, timeout: int = 10):
        source = self.wait_for_element_visible(source_locator, timeout)
        target = self.wait_for_element_visible(target_locator, timeout)
        # Без JS Firefox не хочет перетаскивать ингредиенты
        js_script = """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true
            }));
            target.dispatchEvent(new DragEvent('dragenter', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true
            }));
            target.dispatchEvent(new DragEvent('dragover', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true
            }));
            target.dispatchEvent(new DragEvent('drop', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true
            }));
            source.dispatchEvent(new DragEvent('dragend', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true
            }));
        """
        self.driver.execute_script(js_script, source, target)

    def wait_for_text_in_element(self, locator: tuple, text: str, timeout: int = 10) -> bool:
        try:
            return self._get_wait(timeout).until(
                expected_conditions.text_to_be_present_in_element(locator, text)
            )
        except TimeoutException:
            return False