from selenium.webdriver.common.by import By


class OrdersListPageLocators:
    LAST_ORDER_ITEM = (By.XPATH, "//ul[contains(@class, 'OrderFeed')]//li[1]")
    ORDER_DETAILS_MODAL = (By.XPATH,"//div[contains(@class, 'Modal_orderBox')]")
    TOTAL_ORDERS_COUNTER = (By.XPATH,"//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    TODAY_ORDERS_COUNTER = (By.XPATH,"//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    ORDER_BY_NUMBER_XPATH = "//li[contains(@class, 'OrderHistory_listItem') and .//p[text()='{}']]"