from selenium.webdriver.common.by import By


class LoginPageLocators:

    ERROR_PASSWORD_TEXT = [By.XPATH, ".//p[text()='Некорректный пароль']"]

    ENTER_BUTTON = [By.XPATH, ".//button[contains(text(),'Войти')]"]

    EMAIL_INPUT = [By.XPATH, ".//input[@type='text']"]

    PASSWORD_INPUT = [By.XPATH, ".//input[@type='password']"]

    RECOVER_PASSWORD_TEXT = [By.XPATH, ".//p[text()='Забыли пароль?']"]

    RECOVER_PASSWORD_LINK = [By.XPATH, ".//a[text()='Восстановить пароль']"]

    LOGIN_FORM = [By.XPATH, ".//h2[text()='Вход']"]

    EYE_BUTTON = [By.XPATH, ".//div[@class='input__icon input__icon-action']"]
