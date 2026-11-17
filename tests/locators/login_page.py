from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = (By.XPATH, "//input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")
    RECOVER_PASSWORD_LINK = (By.XPATH,"//a[contains(@class, 'Auth_link') and text()='Восстановить пароль']")