import allure

from locators.history_page_locators import HistoryPageLocators
from pages.BasePage import BasePage
from url import URL

@allure.description('Работаем со страницей истории заказов в личном кабинете.')
class HistoryPage(BasePage):

    @allure.step('Открытие старицы заказов по отдельной ссылке.')
    def history_page_url(self):
        return self.get_url(URL.HISTORY_URL)

    @allure.step('Нажимаем кнопку выход из дичного кабинета')
    def click_logout(self):
        self.find_element_with_wait(HistoryPageLocators.LOCATORS_LOGOUT_BUTTON)
        self.click_on_element(HistoryPageLocators.LOCATORS_LOGOUT_BUTTON)

    @allure.step('Ищем заказ в истории заказов.')
    def find_order(self):
        self.find_element_with_wait(HistoryPageLocators.HISTORY_ORDERS)
        return self.get_text_from_element(HistoryPageLocators.HISTORY_ORDERS)

    @allure.step('Нажимаем лента заказов в шапке страницы.')
    def go_feed_orders(self):
        self.find_element_with_wait(HistoryPageLocators.FEED_ORDERS)
        self.click_on_element(HistoryPageLocators.FEED_ORDERS)
