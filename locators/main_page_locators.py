# Локаторы главной страницы. Все что посчитал нужным.
from selenium.webdriver.common.by import By


class MainPageLocators:

    # FULL_LOAD_PAGE = [By.CSS_SELECTOR, ".BurgerIngredients_ingredients__1N8v2"]
    
    SOUCES = [By.XPATH, "//h2[2][text()='Соусы']"]

    BURGER_SECTION = [By.CLASS_NAME, ".BurgerIngredients_ingredients__1N8v2"]

    BUNS = [By.XPATH, "//h2[1][text()='Булки']"]

    INGREDIENTS = [By.XPATH, "//h2[3][text()='Начинки']"]

    BUN1_INFO = [By.XPATH, "//div/main/section[1]/div[2]/ul[1]/a[1]"]

    INGREDIENT_INFO = [By.XPATH, "//div/h2[text()='Детали ингредиента']"]

    INGREDIENT_INFO_CLOSE_BUTTON  = [By.XPATH, "//div/section[1]/div[1]/button"]

    BUTTON_ENTER_ACCOUNT = [By.XPATH, "//div/button[text()='Войти в аккаунт']"]

    HEADER_PERSONAL_ACCOUNT = [By.XPATH, "//div/header/nav/a/p[text()='Личный Кабинет']"]

    CONSTRUCTOR_ICON = [By.XPATH, "//nav/ul/li[1]/a/p[text()='Конструктор']"]

    CREATE_ORDER = [By.XPATH, "//section[2]/div/button[text()='Оформить заказ']"]

    MAIN_LOGO = [By.XPATH, "//*[@id='root']/div/header/nav/div"]

    BURGER_CONSTRUCTION_SECTION = [By.XPATH, "//div/main/section[2]/ul"]
