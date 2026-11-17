import allure
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page import MainPageLocators
from pages.base_page import BasePage
from config import MAIN_URL


class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver, url=MAIN_URL)

    @allure.step("Перейти в 'Личный Кабинет'")
    def open_lk(self):
        self.click_element(MainPageLocators.LK_LINK)

    @allure.step("Перейти в раздел 'Конструктор'")
    def open_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step("Перейти в раздел 'Лента Заказов'")
    def open_orders_list(self):
        self.click_element(MainPageLocators.ORDERS_LIST_LINK)

    @allure.step("Кликнуть на ингредиент '{ingredient_name}'")
    def click_ingredient(self, ingredient_name: str):
        ingredient_locator = (
            By.XPATH,
            MainPageLocators.INGREDIENT_BY_NAME_XPATH.format(ingredient_name)
        )
        self.click_element(ingredient_locator)

    @allure.step("Проверить, что открыто окно с деталями ингредиента '{expected_name}'")
    def is_ingredient_modal_opened(self, expected_name: str) -> bool:
        if not self.is_element_visible(MainPageLocators.MODAL_WINDOW):
            return False
        try:
            title_el = self.wait_for_element_visible(MainPageLocators.MODAL_INGREDIENT_TITLE)
            return title_el.text == expected_name
        except TimeoutException:
            return False

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить, что модальное окно ингредиента закрыто")
    def is_ingredient_modal_closed(self) -> bool:
        return self.is_element_invisible(MainPageLocators.MODAL_WINDOW)

    @allure.step("Перетащить ингредиент '{ingredient_name}' в конструктор бургера")
    def drag_ingredient_to_constructor(self, ingredient_name: str):
        ingredient_locator = (
            By.XPATH,
            MainPageLocators.INGREDIENT_BY_NAME_XPATH.format(ingredient_name)
        )
        self.drag_and_drop_element(ingredient_locator, MainPageLocators.CONSTRUCTOR_BASKET)

    @allure.step("Проверить, что счётчик ингредиента '{ingredient_name}' равен {expected_count}")
    def is_ingredient_counter_updated(self, ingredient_name: str, expected_count: int) -> bool:
        counter_locator = (
            By.XPATH,
            MainPageLocators.INGREDIENT_COUNTER_BY_NAME_XPATH.format(ingredient_name)
        )
        return self.wait_for_text_in_element(counter_locator, str(expected_count))

    @allure.step("Нажать на кнопку 'Оформить заказ'")
    def click_confirm_order_btn(self):
        self.click_element(MainPageLocators.CONFIRM_ORDER_BTN)

    @allure.step("Проверить, что открыто модальное окно с номером оформленного заказа")
    def is_order_modal_opened(self, timeout: int = 15) -> bool:
        try:
            order_text = self.get_order_number(timeout=timeout)
            return order_text.isdigit()
        except TimeoutException:
            return False

    @allure.step("Получить номер оформленного заказа")
    def get_order_number(self, timeout: int = 20) -> str:
        def _has_real_order_number(driver):
            elements = driver.find_elements(*MainPageLocators.ORDER_NUMBER)
            if not elements:
                return False
            text = elements[0].text.strip()
            return text if (text.isdigit() and text != "9999") else False

        return WebDriverWait(self.driver, timeout).until(
            _has_real_order_number,
            message="Не удалось дождаться реального номера заказа вместо заглушки 9999"
        )