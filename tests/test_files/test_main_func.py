import allure
import pytest
from selenium import webdriver

from pages.main_page import MainPage
from config import MAIN_URL, ORDERS_LIST_LINK


@pytest.mark.usefixtures("login_in_lk")
class TestMainFunc:
    driver: webdriver.Chrome
    main_page: MainPage

    @allure.title("Проверка перехода на Конструктор")
    def test_click_constructor(self):
        self.main_page.open_constructor()
        assert self.main_page.wait_for_url_to_be(MAIN_URL)

    @allure.title("Проверка перехода на Ленту заказов")
    def test_click_orders_list(self):
        self.main_page.open_orders_list()
        assert self.main_page.wait_for_url_to_be(ORDERS_LIST_LINK)

    @allure.title("Проверка клика на ингредиенты")
    @pytest.mark.parametrize(
        "ingredient_name",
        [
            "Краторная булка N-200i",
            "Флюоресцентная булка R2-D3",
            "Соус с шипами Антарианского плоскоходца",
        ]
    )
    def test_click_ingredient_appear_window(self, ingredient_name):
        self.main_page.click_ingredient(ingredient_name)
        assert self.main_page.is_ingredient_modal_opened(ingredient_name)

    @allure.title("Проверка открытия окна с ингредиентом")
    @pytest.mark.parametrize(
        "ingredient_name",
        [
            "Краторная булка N-200i",
            "Флюоресцентная булка R2-D3",
        ]
    )
    def test_close_ingredient_details_modal(self, ingredient_name):
        self.main_page.click_ingredient(ingredient_name)
        self.main_page.close_ingredient_modal()
        assert self.main_page.is_ingredient_modal_closed()

    @allure.title("Проверка увеличения счетчика ингредиента")
    @pytest.mark.parametrize(
        "ingredient_name, expected_count",
        [
            ("Краторная булка N-200i", 2),
            ("Флюоресцентная булка R2-D3", 2),
        ]
    )
    def test_ingredient_counter_increases_after_drag(self, ingredient_name, expected_count):
        self.main_page.drag_ingredient_to_constructor(ingredient_name)
        assert self.main_page.is_ingredient_counter_updated(ingredient_name, expected_count)

    @allure.title("Выполнение заказа")
    @pytest.mark.parametrize(
        "ingredient_name",
        [
            "Краторная булка N-200i",
            "Флюоресцентная булка R2-D3",
        ]
    )
    def test_do_order(self, ingredient_name):
        self.main_page.drag_ingredient_to_constructor(ingredient_name)
        self.main_page.click_confirm_order_btn()
        assert self.main_page.is_order_modal_opened()
