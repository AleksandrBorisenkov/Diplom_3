from selenium.webdriver.common.by import By


class ProfilePageLocators:

    PROFILE_BUTTON_SAVE = [By.XPATH, ".//button[text()='Сохранить']"]

    LOCATORS_LOGOUT_BUTTON = [By.XPATH, ".//button[text()='Выход']"]

    ORDER_HISTORY = [By.XPATH, ".//a[text()='История заказов']"]
