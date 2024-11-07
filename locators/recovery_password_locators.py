from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    EMAIL_INPUT = [By.XPATH, ".//input[@type='text']"]

    RECOVER_PASSWORD_BUTTON = [By.XPATH, ".//button[text()='Восстановить']"]

    EYE_BUTTON = [By.XPATH, ".//div[@class='input__icon input__icon-action']"]

    PASSWORD_INPUT = [By.XPATH, ".//input[@type='password']"]

    RECOVERY_FORM_1 = [By.XPATH, ".//h2[text()='Восстановление пароля']"]

    ACTIVE_FIELD = [By.XPATH,  ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']"]
