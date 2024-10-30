from selenium.webdriver.common.by import By


class FeedPageLocators:

    TOTAL_TEXT = [By.XPATH, "//*[@id='root']/div/main/div/div/div/div[2]/p[1][text()='Выполнено за все время:']"]
    TOTAL_COUNTER = [By.XPATH, "//*[@id='root']/div/main/div/div/div/div[2]/p[2][text()]"]

    TODAY_TEXT = [By.XPATH, "//*[@id='root']/div/main/div/div/div/div[3]/p[1][text()='Выполнено за сегодня:']"]
    TODAY_COUNTER = [By.XPATH, "//*[@id='root']/div/main/div/div/div/div[3]/p[2][text()]"]

    SEARCH_ORDER = [By.XPATH, "//*[@id='root']/div/main/div/div/ul/li/a/div/p[contains(text(),'14')]"]

    CONSTRUCTOR_ICON = [By.XPATH, "//nav/ul/li[1]/a/p[text()='Конструктор']"]

    IN_PROCESS_COUNTER = [By.XPATH, "//*[@id='root']/div/main/div/div/div/div[1]/ul[2]/li[(@class='text text_type_digits-default mb-2') or (starts-with(text(),'14'))]"]

    FIRST_IN_FEED_ORDERS = [By.XPATH, "//*[@id='root']/div/main/div/div/ul/li[1]"]
    WHAT_IN_ORDER_MODAL = [By.XPATH, "//*[@id='root']/div/section[2]/div[1]/div/p[3][text()='Cостав']"]

    HEADER_PERSONAL_ACCOUNT = [By.XPATH, "//div/header/nav/a/p[text()='Личный Кабинет']"]

