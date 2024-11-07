# Локаторы страницы регистрации. Все что посчитал нужным.
from selenium.webdriver.common.by import By


class RegisterPageLocators:

    EMAIL_INPUT = [By.XPATH, ".//label[text()='Email']"]

    NAME_INPUT = [By.XPATH, ".//label[text()='Имя']"]

    PASSWORD_INPUT = [By.XPATH, ".//label[text()='Пароль']"]

    LOCATORS_REG_FORM = [By.XPATH, ".//div/main/div/form"]

    QUASTION_ALLREADY_REG = [By.XPATH, ".//p[text()='Уже зарегистрированы?']"]

    LINK_ALLREADY_REG = [By.XPATH, ".//a[text()='Войти']"]
