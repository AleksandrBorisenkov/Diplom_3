import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.BasePage import BasePage
from url import URL


@allure.description('Работаем со страницей пользователя.')
class ProfilePage(BasePage):

    @allure.step('Инициируем открытие страницы.')
    def profile_page_url(self):
        return self.driver.get(URL.PROFILE_URL)

    @allure.step('Ждем кнопки История заказов и кликаем по ней.')
    def click_history_button(self):
        self.find_element_with_wait(ProfilePageLocators.ORDER_HISTORY)
        self.find_element_to_be_clickable(ProfilePageLocators.ORDER_HISTORY)
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY)
        return self.current_url()

    @allure.step('В личном кабинете находим и нажимаем кнопку Выйти')
    def click_logout_button(self):
        self.find_element_to_be_clickable(ProfilePageLocators.LOCATORS_LOGOUT_BUTTON)
        self.click_on_element(ProfilePageLocators.LOCATORS_LOGOUT_BUTTON)