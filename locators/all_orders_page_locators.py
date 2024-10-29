from selenium.webdriver.common.by import By


class AllOrdersPageLocators:

    TOTALLY_TEXT = [By.XPATH, "//*[@id='root']/div/main/div/div/div/div[2]/p[1][text()='Выполнено за все время:']"]

    ORDERS_FEED = [By.XPATH, "//*[@id='root']/div/main/div/div/div/div[3]/p[1][text()='Выполнено за сегодня:']"]

    SEARCH_ORDER = [By.XPATH, "//*[text()='{}']"]

    CONSTRUCTOR_ICON = [By.XPATH, "//nav/ul/li[1]/a/p[text()='Конструктор']"]