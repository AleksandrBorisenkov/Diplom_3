from selenium.webdriver.common.by import By


class LoginPageLocators:

    ERROR_PASSWORD_TEXT = [By.XPATH, "//form/fieldset[2]/div/p[text()='Некорректный пароль']"]

    ENTER_BUTTON = [By.XPATH, "//button[contains(text(),'Войти')]"]

    EMAIL_INPUT = [By.XPATH, "//input[@type='text']"]

    PASSWORD_INPUT = [By.XPATH, "//input[@type='password']"]

    RECOVER_PASSWORD_TEXT = [By.XPATH, "//div/p[text()='Забыли пароль?']"]

    RECOVER_PASSWORD_LINK = [By.XPATH, "//div/p/a[text()='Восстановить пароль']"]

    LOGIN_FORM = [By.XPATH, "//div/main/div/h2[text()='Вход']"]

    EYE_BUTTON = [By.XPATH, "//fieldset/div/div/div"]
