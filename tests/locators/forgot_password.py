from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    EMAIL_FIELD = (By.XPATH, "//div[contains(@class, 'input')][./label[text()='Email']]/input")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")