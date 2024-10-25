from selenium.webdriver.common.by import By


class ProfilePageLocators:

    PROFILE_BUTTON_SAVE = [By.XPATH, ".//button[2][text()='Сохранить']"]

    LOCATORS_LOGOUT_BUTTON = [By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button[text()='Выход']"]

    ORDER_HISTORY = [By.XPATH, "*//ul/li[2]/a[text()='История заказов']"]
