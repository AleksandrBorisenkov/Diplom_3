import allure

from locators.login_page_locators import LoginPageLocators
from pages.BasePage import BasePage
from url import URL

@allure.description('Работаем со страницей входа в систему.')
class LoginPage(BasePage):

    @allure.step('Инициируем открытие страницы.')
    def login_page_open(self):
        return self.driver.get(URL.LOGIN_URL)

    @allure.step('Получам текст названия формы входа.')
    def wait_login_form(self):
        return self.get_text_from_element(LoginPageLocators.LOGIN_FORM)

    @allure.step('Заполняем форму входа и жмем войти.')
    def fill_login_form(self, mail, password):
        self.set_text_to_element(LoginPageLocators.EMAIL_INPUT, mail)
        self.set_text_to_element(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_on_element(LoginPageLocators.ENTER_BUTTON)

    @allure.step('Кликаем по линку Восстановить пароль.')
    def go_to_password_recovery(self):
        self.click_on_element(LoginPageLocators.RECOVER_PASSWORD_LINK)
