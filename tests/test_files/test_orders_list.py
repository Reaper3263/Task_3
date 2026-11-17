import time

import allure
import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.orders_list_page import OrdersListPage


@pytest.mark.usefixtures("login_in_lk")
class TestOrdersList:
    driver: webdriver.Chrome
    orders_list: OrdersListPage
    main_page: MainPage

    @allure.title("Проверка открытия заказа в ленте")
    def test_click_last_order(self):
        self.orders_list.open()
        self.orders_list.click_last_order()
        assert self.orders_list.is_order_details_modal_opened()

    @allure.title("Проверка появления созданных заказов в ленте")
    def test_user_order_appears(self):
        self.main_page.drag_ingredient_to_constructor("Краторная булка N-200i")
        self.main_page.click_confirm_order_btn()
        order_num = self.main_page.get_order_number()
        self.orders_list.open()
        assert self.orders_list.is_order_present(order_num)

    @allure.title("Проверка повышения счетчика после заказа")
    def test_counter_all_time_increase(self):
        time.sleep(1)   # Без сна сайт почему то разлогинивает сессию пользователя
        self.orders_list.open()
        count_before_all = self.orders_list.get_total_orders_count()
        count_before_today = self.orders_list.get_today_orders_count()
        self.main_page.open()
        self.main_page.drag_ingredient_to_constructor("Краторная булка N-200i")
        self.main_page.click_confirm_order_btn()
        time.sleep(5)   # Для ожидания создания заказа на бекенде
        self.orders_list.open()
        count_after_all = self.orders_list.get_total_orders_count()
        count_after_today = self.orders_list.get_today_orders_count()
        assert count_before_all < count_after_all
        assert count_before_today < count_after_today
