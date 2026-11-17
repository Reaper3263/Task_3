from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")
    TOGLE_VISIBILITY_ICON = (By.XPATH, "//input[@name='Введите новый пароль']/following-sibling::div[contains(@class, 'input__icon')]")