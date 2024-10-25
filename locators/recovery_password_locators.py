from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    EMAIL_INPUT = [By.XPATH, "//input[@type='text']"]

    CODE_FROM_EMAIL = [By.XPATH, "//div/main/div/form/fieldset[2]/div/div/input"]

    RECOVER_PASSWORD_BUTTON = [By.XPATH, "//form/button[text()='Восстановить']"]

    EYE_BUTTON = [By.XPATH, "//fieldset/div/div/div"]

    PASSWORD_INPUT = [By.XPATH, "//input[@type='password']"]

    RECOVERY_FORM_1 = [By.XPATH, "//div/main/div/h2[text()='Восстановление пароля']"]

    ACTIVE_FIELD = [By.XPATH,  "//div/form/fieldset[1]/div/div/input[@type='text']"]