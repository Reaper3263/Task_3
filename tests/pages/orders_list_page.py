import time

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from locators.orders_list_page import OrdersListPageLocators
from pages.base_page import BasePage
from config import ORDERS_LIST_LINK


class OrdersListPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver, url=ORDERS_LIST_LINK)

    def _get_order_locator_by_number(self, order_number: str) -> tuple:
        formatted_number = order_number if order_number.startswith("#") else f"#{order_number.zfill(6)}"
        return (
            By.XPATH,
            OrdersListPageLocators.ORDER_BY_NUMBER_XPATH.format(formatted_number)
        )

    @allure.step("Проверить наличие заказа №{order_number} в ленте")
    def is_order_present(
            self,
            order_number: str,
            timeout: int = 20,
            refresh_interval: int = 4
    ) -> bool:
        locator = self._get_order_locator_by_number(order_number)
        end_time = time.monotonic() + timeout

        while time.monotonic() < end_time:
            if self.is_element_visible(locator, timeout=refresh_interval):
                return True

            if time.monotonic() < end_time:
                self.driver.refresh()

        return False

    @allure.step("Открыть детали заказа №{order_number}")
    def click_order_by_number(self, order_number: str):
        locator = self._get_order_locator_by_number(order_number)
        self.click_element(locator)

    @allure.step("Кликнуть на последний заказ в ленте")
    def click_last_order(self):
        self.click_element(OrdersListPageLocators.LAST_ORDER_ITEM)

    @allure.step("Проверить, что открыто модальное окно с деталями заказа")
    def is_order_details_modal_opened(self) -> bool:
        return self.is_element_visible(OrdersListPageLocators.ORDER_DETAILS_MODAL)

    @allure.step("Получить счётчик 'Выполнено за все время'")
    def get_total_orders_count(self) -> int:
        el = self.wait_for_element_visible(OrdersListPageLocators.TOTAL_ORDERS_COUNTER)
        return int(el.text)

    @allure.step("Получить счётчик 'Выполнено за сегодня'")
    def get_today_orders_count(self) -> int:
        el = self.wait_for_element_visible(OrdersListPageLocators.TODAY_ORDERS_COUNTER)
        return int(el.text)
