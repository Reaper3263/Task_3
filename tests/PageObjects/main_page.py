from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.base_page import BasePage
from config import MAIN_URL


class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver, url=MAIN_URL)

        self.lk_link = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")
        self.constructor_link = (By.XPATH, "//a[.//p[text()='Конструктор']]")
        self.orders_list_link = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")

        self.modal_window = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")
        self.modal_ingredient_title = (
            By.XPATH,
            "//div[contains(@class, 'Modal_modal__contentBox')]//p[contains(@class, 'text_type_main-medium')]"
        )
        self.modal_close_button = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
        self.constructor_basket = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
        self.confirm_order_btn = (By.XPATH, "//button[text()='Оформить заказ']")
        self.order_number = (
            By.XPATH,
            "//div[contains(@class, 'Modal_modal__contentBox')]//h2[contains(@class, 'text_type_digits-large')]"
        )

    def open_lk(self):
        self.click_element(self.lk_link)

    def open_constructor(self):
        self.click_element(self.constructor_link)

    def open_orders_list(self):
        self.click_element(self.orders_list_link)

    def click_ingredient(self, ingredient_name: str):
        ingredient_locator = (
            By.XPATH,
            f"//a[contains(@class, 'BurgerIngredient_ingredient') and .//p[text()='{ingredient_name}']]"
        )
        self.click_element(ingredient_locator)

    def is_ingredient_modal_opened(self, expected_name: str) -> bool:
        if not self.is_element_visible(self.modal_window):
            return False
        try:
            title_el = self.wait_for_element_visible(self.modal_ingredient_title)
            return title_el.text == expected_name
        except TimeoutException:
            return False

    def close_ingredient_modal(self):
        self.click_element(self.modal_close_button)

    def is_ingredient_modal_closed(self) -> bool:
        return self.is_element_invisible(self.modal_window)

    def drag_ingredient_to_constructor(self, ingredient_name: str):
        ingredient_locator = (
            By.XPATH,
            f"//a[contains(@class, 'BurgerIngredient_ingredient') and .//p[text()='{ingredient_name}']]"
        )
        self.drag_and_drop_element(ingredient_locator, self.constructor_basket)

    def is_ingredient_counter_updated(self, ingredient_name: str, expected_count: int) -> bool:
        counter_locator = (
            By.XPATH,
            f"//a[contains(@class, 'BurgerIngredient_ingredient') and .//p[text()='{ingredient_name}']]//p[contains(@class, 'counter_counter__num')]"
        )
        return self.wait_for_text_in_element(counter_locator, str(expected_count))

    def click_confirm_order_btn(self):
        self.click_element(self.confirm_order_btn)

    def is_order_modal_opened(self, timeout: int = 15) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until_not(
                expected_conditions.text_to_be_present_in_element(self.order_number, "9999")
            )
            order_text = self.wait_for_element_visible(self.order_number).text
            return order_text.isdigit()
        except TimeoutException:
            return False

    def get_order_number(self, timeout: int = 15) -> str:
        WebDriverWait(self.driver, timeout).until_not(
            expected_conditions.text_to_be_present_in_element(self.order_number, "9999")
        )
        order_el = self.wait_for_element_visible(self.order_number)
        return order_el.text