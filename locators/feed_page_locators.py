from selenium.webdriver.common.by import By


class FeedPageLocators:

    TOTAL_TEXT = [By.XPATH, ".//p[text()='Выполнено за все время:']"]
    TOTAL_COUNTER = [By.XPATH, ".//div[@class='undefined mb-15']/p[contains(text(),'15')]"]

    TODAY_TEXT = [By.XPATH, ".//p[text()='Выполнено за сегодня:']"]
    TODAY_COUNTER = [By.XPATH, ".//div[last()]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"]

    SEARCH_ORDER = [By.XPATH, ".//p[@class='text text_type_digits-default' and contains(text(),'15')]"]

    CONSTRUCTOR_ICON = [By.XPATH, ".//p[text()='Конструктор']"]

    IN_PROCESS_COUNTER = [By.XPATH,".//li[(@class='text text_type_digits-default mb-2')]/parent::ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']"]

    FIRST_IN_FEED_ORDERS = [By.XPATH, ".//li[@class='OrderHistory_listItem__2x95r mb-6']/a[@class='OrderHistory_link__1iNby']"]
    WHAT_IN_ORDER_MODAL = [By.XPATH, ".//p[text()='Cостав']"]

    HEADER_PERSONAL_ACCOUNT = [By.XPATH, ".//p[text()='Личный Кабинет']"]

