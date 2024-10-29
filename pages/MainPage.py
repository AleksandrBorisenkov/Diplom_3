import time

import allure

from locators.main_page_locators import MainPageLocators
from pages.BasePage import BasePage
from url import URL

@allure.description('Работаем с главной страницей. Тут вся магия: работа с ингредиентами, создать заказ войти в личный кабинет.')
class MainPage(BasePage):

    @allure.step('Инициируем открытие страницы.')
    def main_page_open(self):
        return self.driver.get(URL.MAIN_URL)

    @allure.step('Ожидаем появление булок.')
    def wait_buns(self):
        self.find_elements_with_wait(MainPageLocators.BUNS_LOGOS)
        self.find_element_with_wait(MainPageLocators.BUNS)

    @allure.step('Ищем и жмем Личный кабинет.')
    def find_and_click_profile_link(self):
        self.find_element_to_be_clickable(MainPageLocators.HEADER_PERSONAL_ACCOUNT)
        self.click_on_element(MainPageLocators.HEADER_PERSONAL_ACCOUNT)

    @allure.step('Ищем и жмем кнопку Войти в аккаунт (там где собирается бургер).')
    def click_enter_account(self):
        self.find_elements_with_wait(MainPageLocators.BUTTON_ENTER_ACCOUNT)
        self.click_on_element(MainPageLocators.BUTTON_ENTER_ACCOUNT)

    @allure.step('Жмем кнопу оформить заказ (доступно если залогинен).')
    def click_create_order(self):
        self.find_element_with_wait(MainPageLocators.CREATE_ORDER)
        self.click_on_element(MainPageLocators.CREATE_ORDER)

    @allure.step('Берем номер заказа и сохраняем его для дальнейшего использования.')
    def wait_order_modal_counter(self):
        order_num = []
        self.find_element_with_wait(MainPageLocators.CREATE_ORDER_MODAL_COUNTER)
        order_num.append(self.get_text_from_element(MainPageLocators.CREATE_ORDER_MODAL_COUNTER))
        return order_num

    @allure.step('Жмем на карточку булки и получаем модалку с деталями ингридиента.')
    def click_on_ingredients(self):
        self.find_element_with_wait(MainPageLocators.BUN1_INFO_CARD)
        self.click_on_element(MainPageLocators.BUN1_INFO_CARD)

    @allure.step('Получили текст модального окна.')
    def get_text_ingredients_module(self):
        self.find_element_with_wait(MainPageLocators.INGREDIENT_INFO_MODAL_ACTIVE)
        self.find_element_with_wait(MainPageLocators.INGREDIENT_INFO_TEXT)
        self.get_text_from_element(MainPageLocators.INGREDIENT_INFO_TEXT)
        return self.get_text_from_element(MainPageLocators.INGREDIENT_INFO_TEXT)


    @allure.step('Закрываем модалку ингридиентов.')
    def close_info_ingredients(self):
        self.find_element_with_wait(MainPageLocators.INGREDIENT_INFO_MODAL_ACTIVE)
        self.click_on_element(MainPageLocators.INGREDIENT_INFO_CLOSE_BUTTON)
        self.find_element_with_wait(MainPageLocators.INGREDIENT_INFO_MODAL_HIDE)

    @allure.step('Жмем Лента заказов.')
    def click_feed_orders(self):
        self.find_element_with_wait(MainPageLocators.FEED_ORDERS)
        self.click_on_element(MainPageLocators.FEED_ORDERS)

    @allure.step('Перетаскиваем булку в область конструктора.')
    def drag_and_drop_element(self):
        return self.drag_and_drop(MainPageLocators.BUN2_DRAG,MainPageLocators.CONSTRUCTOR_DROP)

    def get_counter_text(self):
        return self.get_text_from_element(MainPageLocators.COUNTER)
