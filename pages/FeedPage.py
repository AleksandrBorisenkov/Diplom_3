import allure

from locators.feed_page_locators import FeedPageLocators
from pages.BasePage import BasePage
from url import URL

@allure.description('Работаем со страницей заказов.')
class AllOrdersPage(BasePage):

    @allure.step('Инициируем открытие страницы.')
    def feed_page_open(self):
        return self.driver.get(URL.ALL_ORDERS_URL)

    @allure.step('Ищем текст с общим количеством заказов.')
    def find_total_text(self):
        self.find_element_with_wait(FeedPageLocators.TOTAL_TEXT)
        return self.get_text_from_element(FeedPageLocators.TOTAL_TEXT)

    @allure.step('Берем количество счетчика за все время.')
    def find_total_counter(self):
        self.find_element_with_wait(FeedPageLocators.TOTAL_COUNTER)
        return self.get_text_from_element(FeedPageLocators.TOTAL_COUNTER)

    @allure.step('Ищем текст с количеством заказов за сегодня.')
    def find_today_text(self):
        self.find_elements_with_wait(FeedPageLocators.TODAY_TEXT)
        return self.get_text_from_element(FeedPageLocators.TODAY_TEXT)

    @allure.step('Берем количество счетчика за сегодня.')
    def find_today_counter(self):
        self.find_element_with_wait(FeedPageLocators.TODAY_COUNTER)
        return self.get_text_from_element(FeedPageLocators.TODAY_COUNTER)

    @allure.step('Получаем значение из раздела В работе.')
    def order_in_progress(self):
        self.find_element_with_wait(FeedPageLocators.IN_PROCESS_COUNTER)
        return self.get_text_from_element(FeedPageLocators.IN_PROCESS_COUNTER)

    @allure.step('Щелкаем на иконку Конструктор для возврата на главную страницу.')
    def click_to_constructor_icon(self):
        self.find_element_with_wait(FeedPageLocators.CONSTRUCTOR_ICON)
        self.click_on_element(FeedPageLocators.CONSTRUCTOR_ICON)

    @allure.step('Кликаем на первый заказ в списке и открываем состав заказа.')
    def click_first_in_feed_orders(self):
        self.find_element_with_wait(FeedPageLocators.FIRST_IN_FEED_ORDERS)
        self.click_on_element(FeedPageLocators.FIRST_IN_FEED_ORDERS)
        self.find_element_with_wait(FeedPageLocators.WHAT_IN_ORDER_MODAL)
        return self.get_text_from_element(FeedPageLocators.WHAT_IN_ORDER_MODAL)

    @allure.step('Переход в личный кабинет.')
    def click_personal_account(self):
        self.find_element_with_wait(FeedPageLocators.HEADER_PERSONAL_ACCOUNT)
        self.click_on_element(FeedPageLocators.HEADER_PERSONAL_ACCOUNT)

    @allure.step('Поиск заказа пользователя в ленте заказов.')
    def search_user_order(self):
        self.find_elements_with_wait(FeedPageLocators.SEARCH_ORDER)
        return self.get_text_from_element(FeedPageLocators.SEARCH_ORDER)
