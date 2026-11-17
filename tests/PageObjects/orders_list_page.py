from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from PageObjects.base_page import BasePage
from config import ORDERS_LIST_LINK


class OrdersListPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver, url=ORDERS_LIST_LINK)
        self.last_order_item = (
            By.XPATH,
            "//ul[contains(@class, 'OrderFeed')]//li[1]"
        )
        self.order_details_modal = (
            By.XPATH,
            "//div[contains(@class, 'Modal_orderBox')]"
        )
        self.total_orders_counter = (
            By.XPATH,
            "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]"
        )
        self.today_orders_counter = (
            By.XPATH,
            "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]"
        )

    def _get_order_locator_by_number(self, order_number: str) -> tuple:
        formatted_number = order_number if order_number.startswith("#") else f"#{order_number.zfill(6)}"

        return (
            By.XPATH,
            f"//li[contains(@class, 'OrderHistory_listItem') and .//p[text()='{formatted_number}']]"
        )

    def is_order_present(self, order_number: str) -> bool:
        locator = self._get_order_locator_by_number(order_number)
        return self.is_element_visible(locator)

    def click_order_by_number(self, order_number: str):
        locator = self._get_order_locator_by_number(order_number)
        self.click_element(locator)

    def click_last_order(self):
        self.click_element(self.last_order_item)

    def is_order_details_modal_opened(self) -> bool:
        return self.is_element_visible(self.order_details_modal)

    def get_total_orders_count(self) -> int:
        el = self.wait_for_element_visible(self.total_orders_counter)
        return int(el.text)

    def get_today_orders_count(self) -> int:
        el = self.wait_for_element_visible(self.today_orders_counter)
        return int(el.text)
