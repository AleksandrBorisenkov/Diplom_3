# Локаторы главной страницы. Все что посчитал нужным.
from selenium.webdriver.common.by import By


class MainPageLocators:

    SOUCES = [By.XPATH, "//h2[2][text()='Соусы']"]

    BURGER_SECTION = [By.CLASS_NAME, ".BurgerIngredients_ingredients__1N8v2"]

    BUNS = [By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/h2[1][text()='Булки']"]

    BUNS_LOGOS = [By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[1]"]

    BUN2_DRAG = [By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[2]"]

    CONSTRUCTOR_DROP = [By.XPATH, "//*[@id='root']/div/main/section[2]/ul"]

    INGREDIENTS = [By.XPATH, "//h2[3][text()='Начинки']"]

    BUN1_INFO_CARD = [By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[1]"]

    INGREDIENT_INFO_MODAL_ACTIVE= [By.XPATH, "//*[@id='root']/div/section[1][@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"]

    INGREDIENT_INFO_MODAL_HIDE = [By.XPATH, "//*[@id='root']/div/section[1][@class='Modal_modal__P3_V5']"]

    INGREDIENT_INFO_TEXT = [By.XPATH, "//div/h2[text()='Детали ингредиента']"]

    INGREDIENT_INFO_CLOSE_BUTTON  = [By.XPATH, "//div/section[1]/div[1]/button"]

    BUTTON_ENTER_ACCOUNT = [By.XPATH, "//div/button[text()='Войти в аккаунт']"]

    HEADER_PERSONAL_ACCOUNT = [By.XPATH, "//div/header/nav/a/p[text()='Личный Кабинет']"]

    CONSTRUCTOR_ICON = [By.XPATH, "//nav/ul/li[1]/a/p[text()='Конструктор']"]

    CREATE_ORDER = [By.XPATH, "//section[2]/div/button[text()='Оформить заказ']"]

    BURGER_CONSTRUCTION_SECTION = [By.XPATH, "//div/main/section[2]/ul"]

    FEED_ORDERS = [By.XPATH, "//*[@id='root']/div/header/nav/ul/li[2]/a/p[text()='Лента Заказов']"]

    COUNTER = [By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[2]/div[1]/p[text()]"]

    CREATE_ORDER_MODAL_COUNTER = [By.XPATH, "//*[@id='root']/div/section/div[1]/div/h2[text()]"]