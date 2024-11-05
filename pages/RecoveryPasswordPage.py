import allure
from allure_pytest.utils import ALLURE_LINK_MARK

from locators.recovery_password_locators import ForgotPasswordPageLocators
from pages.BasePage import BasePage
from url import URL

@allure.description('Проверяем страницу восстановления пароля.')
class RecoveryPasswordPage(BasePage):

    @allure.step('Открываем страницу Восстановить пароль.')
    def recovery_password_page_url(self):
        return self.get_url(URL.RECOVERY_PAS_URL)

    @allure.step('ждем загрузки формы.')
    def wait_recovery_form_only_email(self):
        self.find_element_with_wait(ForgotPasswordPageLocators.RECOVERY_FORM_1)

    @allure.step('Заполняем почту и жмем Восстановить.')
    def fill_email_recovery(self, email):
        self.set_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT, email)
        self.click_on_element(ForgotPasswordPageLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step('В поле Пароль жмем на глаз и ловим, что поле подсветилось.')
    def active_field_password(self):
        self.click_on_element(ForgotPasswordPageLocators.EYE_BUTTON)
        self.find_element_with_wait(ForgotPasswordPageLocators.ACTIVE_FIELD)

    @allure.step('Сверяем что поле стало активным')
    def active_field_or_not(self):
        active = self.find_element_with_wait(ForgotPasswordPageLocators.ACTIVE_FIELD) != self.find_element_with_wait(
            ForgotPasswordPageLocators.PASSWORD_INPUT)
        return active