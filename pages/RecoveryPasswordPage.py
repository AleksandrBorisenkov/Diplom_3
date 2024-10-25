import allure

from locators.recovery_password_locators import ForgotPasswordPageLocators
from pages.BasePage import BasePage
from url import URL


class RecoveryPasswordPage(BasePage):

    def recovery_password_page_url(self):
        return self.driver.get(URL.RECOVERY_PAS_URL)

    def wait_recovery_form_only_email(self):
        self.find_element_with_wait(ForgotPasswordPageLocators.RECOVERY_FORM_1)

    def fill_email_recovery(self, email):
        self.set_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT, email)
        self.click_on_element(ForgotPasswordPageLocators.RECOVER_PASSWORD_BUTTON)

    def active_field_password(self):
        self.click_on_element(ForgotPasswordPageLocators.EYE_BUTTON)
        self.find_element_with_wait(ForgotPasswordPageLocators.ACTIVE_FIELD)
