from selenium.webdriver.common.by import By


class HistoryPageLocators:

    LOCATORS_LOGOUT_BUTTON = [By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button[text()='Выход']"]

    HISTORY_ORDERS = [By.XPATH, "//*[@id='root']/div/main/div/div/div/ul/li[last()]/a/div[1]/p[1][contains(text(),'14')]"]

    FEED_ORDERS = [By.XPATH, "//*[@id='root']/div/header/nav/ul/li[2]/a/p[text()='Лента Заказов']"]
