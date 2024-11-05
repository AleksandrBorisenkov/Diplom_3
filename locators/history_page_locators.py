from selenium.webdriver.common.by import By


class HistoryPageLocators:

    LOCATORS_LOGOUT_BUTTON = [By.XPATH, ".//button[text()='Выход']"]

    HISTORY_ORDERS = [By.XPATH, ".//div/ul/li[last()]/a/div[1]/p[1][contains(text(),'15')]"]

    FEED_ORDERS = [By.XPATH, ".//p[text()='Лента Заказов']"]
