from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    EMAIL_INPUT = [By.XPATH, "//input[@type='text']"]

    CODE_FROM_EMAIL = [By.XPATH, "//div/main/div/form/fieldset[2]/div/div/input"]

    RECOVER_PASSWORD_BUTTON = [By.XPATH, "//form/button[text()='Восстановить']"]

    EYE_BUTTON = [By.XPATH, "//fieldset/div/div/div"]

    ACTIVE_FIELD= [By.CSS_SELECTOR, ".input_status_active"]

    PASSWORD_INPUT = [By.XPATH, "//input[@type='password']"]

    RECOVERY_FORM_1 = [By.XPATH, "//div/main/div/h2[text()='Восстановление пароля']"]
# input pr-6 pl-6 input_type_text input_size_default input_status_active