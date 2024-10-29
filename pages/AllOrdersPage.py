import allure

from locators.all_orders_page_locators import AllOrdersPageLocators
from pages.BasePage import BasePage
from url import URL

@allure.description('Работаем со страницей заказов.')
class AllOrdersPage(BasePage):

    @allure.step('Инициируем открытие страницы.')
    def all_orders_page_url(self):
        return self.driver.get(URL.ALL_ORDERS_URL)

    @allure.step('Ищем текст с общим количеством заказов.')
    def find_totaly_sum(self):
        self.find_element_with_wait(AllOrdersPageLocators.TOTALLY_TEXT)
        return self.get_text_from_element(AllOrdersPageLocators.TOTALLY_TEXT)

    @allure.step('Ищем текст с количеством заказов за сегодня.')
    def find_today_sum(self):
        self.find_elements_with_wait(AllOrdersPageLocators.ORDERS_FEED)
        return self.get_text_from_element(AllOrdersPageLocators.ORDERS_FEED)

    @allure.step('Щелкаем на иконку Конструктор для возврата на главную старницу')
    def click_to_constructor_icon(self):
        self.find_element_with_wait(AllOrdersPageLocators.CONSTRUCTOR_ICON)
        self.click_on_element(AllOrdersPageLocators.CONSTRUCTOR_ICON)
