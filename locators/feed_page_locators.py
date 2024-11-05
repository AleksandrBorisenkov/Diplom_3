from selenium.webdriver.common.by import By


class FeedPageLocators:

    TOTAL_TEXT = [By.XPATH, ".//p[text()='Выполнено за все время:']"]
    TOTAL_COUNTER = [By.XPATH, ".//div/div/div/div[2]/p[2][text()]"]

    TODAY_TEXT = [By.XPATH, ".//p[text()='Выполнено за сегодня:']"]
    TODAY_COUNTER = [By.XPATH, ".//div/div/div/div[3]/p[2][text()]"]

    SEARCH_ORDER = [By.XPATH, ".//li/a/div/p[contains(text(),'15')]"]

    CONSTRUCTOR_ICON = [By.XPATH, ".//p[text()='Конструктор']"]

    IN_PROCESS_COUNTER = [By.XPATH, ".//div[1]/ul[2]/li[(@class='text text_type_digits-default mb-2') or (starts-with(text(),'15'))]"]

    FIRST_IN_FEED_ORDERS = [By.XPATH, ".//main/div/div/ul/li[1]"]
    WHAT_IN_ORDER_MODAL = [By.XPATH, ".//p[3][text()='Cостав']"]

    HEADER_PERSONAL_ACCOUNT = [By.XPATH, ".//p[text()='Личный Кабинет']"]

