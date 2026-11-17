from selenium.webdriver.common.by import By


class MainPageLocators:
    LK_LINK = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")
    CONSTRUCTOR_LINK = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    ORDERS_LIST_LINK = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")

    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")
    MODAL_INGREDIENT_TITLE = (By.XPATH,"//div[contains(@class, 'Modal_modal__contentBox')]//p[contains(@class, 'text_type_main-medium')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    CONSTRUCTOR_BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    CONFIRM_ORDER_BTN = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER = (By.XPATH,"//div[contains(@class, 'Modal_modal__contentBox')]//h2[contains(@class, 'text_type_digits-large')]")

    INGREDIENT_BY_NAME_XPATH = "//a[contains(@class, 'BurgerIngredient_ingredient') and .//p[text()='{}']]"
    INGREDIENT_COUNTER_BY_NAME_XPATH = ("//a[contains(@class, 'BurgerIngredient_ingredient') and .//p[text()='{}']]""//p[contains(@class, 'counter_counter__num')]")