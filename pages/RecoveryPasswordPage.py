import allure

from locators.recovery_password_locators import ForgotPasswordPageLocators
from pages.BasePage import BasePage


class RecoveryPasswordPage(BasePage):

    def wait_recovery_form_only_email(self):
        self.find_element_with_wait(ForgotPasswordPageLocators.RECOVERY_FORM_1)

    def fill_email_recovery(self, email):
        self.set_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT, email)
        self.click_on_element(ForgotPasswordPageLocators.RECOVER_PASSWORD_BUTTON)

    def active_field_password(self):
        self.click_on_element(ForgotPasswordPageLocators.EYE_BUTTON)
        self.find_element_with_wait(ForgotPasswordPageLocators.ACTIVE_FIELD)
        # self.get_color(ForgotPasswordPageLocators.PASSWORD_INPUT, )