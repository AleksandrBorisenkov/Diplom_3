import time

import allure

from locators.all_orders_page_locators import AllOrdersPageLocators
from locators.main_page_locators import MainPageLocators
from pages.AllOrdersPage import AllOrdersPage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from url import URL


@allure.description('Проверяем работу главной страницы. Включая оформления заказа и получение его номера.')
class TestMainPage:

    @allure.title('Проверяем переход с главной в ленту заказов и обратно в конструктор на главную.')
    def test_from_constructor_to_feed_and_back(self, driver):
        main_page = MainPage(driver)
        feed_page = AllOrdersPage(driver)
        # сверху прогружаем драйверы всех страницы участниц
        # ниже сам тест
        main_page.main_page_open()
        assert main_page.current_url() == URL.MAIN_URL
        main_page.click_feed_orders()
        feed_page.all_orders_page_url()
        assert feed_page.current_url() == URL.ALL_ORDERS_URL
        assert "Выполнено за все время:" in feed_page.find_totaly_sum()
        assert "Выполнено за сегодня:" in feed_page.find_today_sum()
        feed_page.click_to_constructor_icon()
        assert main_page.current_url() == URL.MAIN_URL

    @allure.title('На главной странице жмем на булку, ловим модалку, закрываем и проверяем что она закрыта.')
    def test_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        # сверху прогружаем драйверы всех страницы участниц
        # ниже сам тест
        main_page.main_page_open()
        main_page.wait_buns()
        main_page.click_on_ingredients()
        assert "Детали ингредиента" in main_page.get_text_ingredients_module()
        assert MainPageLocators.INGREDIENT_INFO_MODAL_ACTIVE != main_page.close_info_ingredients()

    @allure.title('Перетащили булку в конструктор и счетчик на иконке булки должен показать цифру 2.')
    def test_add_ingredient_in_constructor(self, driver):
        main_page = MainPage(driver)
        # сверху прогружаем драйверы всех страницы участниц
        # ниже сам тест
        main_page.main_page_open()
        main_page.drag_and_drop_element()
        assert '2' in main_page.get_counter_text()

    @allure.title('Логинемся, добавляем булку в конструктор и оформляем заказ ожидая номера заказа != 9999.')
    def test_login_user_push_create_order(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        # сверху прогружаем драйверы всех страницы участниц
        # ниже сам тест
        login_page.login_page_open()
        assert login_page.current_url() == URL.LOGIN_URL
        assert 'Вход' in login_page.wait_login_form()
        login_page.fill_login_form('51253@yandex.ru', '12613612')
        main_page.drag_and_drop_element()
        assert '2' in main_page.get_counter_text()
        main_page.click_create_order()
        time.sleep(3) # Знаю, плохо использовать такое. Но ничего другое не помогало.
        assert main_page.wait_order_modal_counter() != '9999'

# @allure.description('Проверка создания ')
# class TestFeedOrders:


