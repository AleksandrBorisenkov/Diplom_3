import allure

from data_help import exist_user_email, exist_user_password
from pages.FeedPage import AllOrdersPage
from pages.HistoryPage import HistoryPage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.ProfilePage import ProfilePage
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
        main_page.click_feed_orders()
        feed_page.click_to_constructor_icon()
        assert 'Булки' in main_page.get_text_buns()

    @allure.title('На главной странице жмем на булку, ловим модалку, закрываем и проверяем что она закрыта.')
    def test_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        # сверху прогружаем драйверы всех страницы участниц
        # ниже сам тест
        main_page.main_page_open()
        main_page.wait_buns()
        main_page.click_on_ingredients()
        assert "Детали ингредиента" in main_page.get_text_ingredients_module()
        assert main_page.close_info_ingredients() != main_page.check_hide_info_ingredients_modal

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
        login_page.fill_login_form(exist_user_email, exist_user_password)
        main_page.drag_and_drop_element()
        assert '2' in main_page.get_counter_text()
        main_page.click_create_order()
        assert main_page.wait_order_modal_counter() != '9999'

    @allure.title('Логинемся, создаем заказ, идем в ленту заказов ищем его в Работе. Щелкаем на первый заказ из списка - убедились что открылась нужная модалка.')
    def test_check_number_in_feed_orders(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        feed_page = AllOrdersPage(driver)
        # сверху прогружаем драйверы всех страницы участниц
        # ниже сам тест
        login_page.login_page_open()
        login_page.fill_login_form(exist_user_email, exist_user_password)
        main_page.drag_and_drop_element()
        main_page.click_create_order()
        get_order_num = main_page.wait_order_modal_counter()
        assert get_order_num != '9999'
        main_page.close_order_modal_counter()
        main_page.click_feed_orders()
        assert get_order_num == feed_page.find_total_counter()
        assert get_order_num in feed_page.order_in_progress()
        assert "Cостав" in feed_page.click_first_in_feed_orders()

    @allure.title('Взяли значения из ленты заказов, залогинились, создали заказ и проверили, увеличение счетчиков заказов.')
    def test_check_change_total_today_counter(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        feed_page = AllOrdersPage(driver)
        # сверху прогружаем драйверы всех страницы участниц
        # ниже сам тест
        feed_page.feed_page_open()
        total_counter = feed_page.find_total_counter()
        today_counter = feed_page.find_today_counter()
        feed_page.click_personal_account()
        login_page.fill_login_form(exist_user_email, exist_user_password)
        main_page.drag_and_drop_element()
        assert '2' in main_page.get_counter_text()
        main_page.click_create_order()
        get_order_num = main_page.wait_order_modal_counter()
        assert get_order_num != '9999'
        main_page.close_order_modal_counter()
        main_page.click_feed_orders()
        total_counter_new = feed_page.find_total_counter()
        today_counter_new = feed_page.find_today_counter()
        assert total_counter_new > total_counter
        assert today_counter_new > today_counter

    @allure.title('Создаем заказ, проверяем в личном кабинете, проверяем в ленте заказов.')
    def test_order_from_history_exist_in_feed_orders(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        feed_page = AllOrdersPage(driver)
        profile_page = ProfilePage(driver)
        history_page = HistoryPage(driver)
        # сверху прогружаем драйверы всех страницы участниц
        # ниже сам тест
        login_page.login_page_open()
        login_page.fill_login_form(exist_user_email, exist_user_password)
        main_page.drag_and_drop_element()
        main_page.click_create_order()
        get_order_num = main_page.wait_order_modal_counter()
        assert get_order_num != '9999'
        main_page.close_order_modal_counter()
        main_page.find_and_click_profile_link()
        profile_page.click_history_button()
        assert get_order_num in history_page.find_order()
        history_page.go_feed_orders()
        assert get_order_num in feed_page.search_user_order()
