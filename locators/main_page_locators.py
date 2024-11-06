# Локаторы главной страницы. Все что посчитал нужным.
from selenium.webdriver.common.by import By


class MainPageLocators:

    SOUCES = [By.XPATH, ".//h2[text()='Соусы']"]

    BURGER_SECTION = [By.CLASS_NAME, ".BurgerIngredients_ingredients__1N8v2"]

    BUNS = [By.XPATH, ".//h2[text()='Булки']"]

    BUNS_LOGOS = [By.XPATH, ".//ul[@class='BurgerIngredients_ingredients__list__2A-mT']"]

    BUN2_DRAG = [By.XPATH, ".//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']/p[contains(text(),'Краторная')]"]

    CONSTRUCTOR_DROP = [By.XPATH, ".//ul[@class='BurgerConstructor_basket__list__l9dp_']"]

    INGREDIENTS = [By.XPATH, ".//h2[text()='Начинки']"]

    BUN1_INFO_CARD = [By.XPATH, ".//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']/p[contains(text(),'Флюоресцентная')]"]

    INGREDIENT_INFO_MODAL_ACTIVE= [By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"]

    INGREDIENT_INFO_MODAL_HIDE = [By.XPATH, ".//section[@class='Modal_modal__P3_V5']//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']"]

    INGREDIENT_INFO_TEXT = [By.XPATH, ".//h2[text()='Детали ингредиента']"]

    INGREDIENT_INFO_CLOSE_BUTTON  = [By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button"]

    BUTTON_ENTER_ACCOUNT = [By.XPATH, ".//button[text()='Войти в аккаунт']"]

    HEADER_PERSONAL_ACCOUNT = [By.XPATH, ".//p[text()='Личный Кабинет']"]

    CONSTRUCTOR_ICON = [By.XPATH, ".//p[text()='Конструктор']"]

    CREATE_ORDER = [By.XPATH, ".//button[text()='Оформить заказ']"]

    FEED_ORDERS = [By.XPATH, ".//p[text()='Лента Заказов']"]

    COUNTER = [By.XPATH, ".//p[contains(text(),'Краторная')]/parent::*/div/p[@class='counter_counter__num__3nue1' and contains(text(),'')]"]

    CREATE_ORDER_MODAL_COUNTER = [By.XPATH, ".//h2[contains(text(),'15')]"]
    CLOSE_ORDER_MODAL_COUNTER = [By.XPATH, ".//button[@type='button']"]
