# Локаторы страницы регистрации. Все что посчитал нужным.
from selenium.webdriver.common.by import By


class RegisterPageLocators:

    EMAIL_INPUT = [By.XPATH, "//div/div/label[text()='Email']"]

    NAME_INPUT = [By.XPATH, "//div/div/label[text()='Имя']"]

    PASSWORD_INPUT = [By.XPATH, "//div/div/label[text()='Пароль']"]

    LOCATORS_REG_FORM = [By.XPATH, "//*[@id='root']/div/main/div/form"]

    QUASTION_ALLREADY_REG = [By.XPATH, "//div/p[text()='Уже зарегистрированы?']"]

    LINK_ALLREADY_REG = [By.XPATH, "//div/p/a[text()='Войти']"]
