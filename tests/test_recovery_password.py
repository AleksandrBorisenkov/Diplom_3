import time
import pytest
import allure

from locators.recovery_password_locators import ForgotPasswordPageLocators
from pages.LoginPage import LoginPage
from pages.RecoveryPasswordPage import RecoveryPasswordPage
from url import URL
from data_help import mail_generator


@allure.description('Заходим на страницу логина,')
class TestRecoveryPassword:

    def test_recovery_password_from_login_page(self, driver):
        login_page = LoginPage(driver)
        recovery_page = RecoveryPasswordPage(driver)

        login_page.login_page_open()
        login_page.go_to_password_recovery()
        recovery_page.fill_email_recovery(mail_generator())
        time.sleep(1)
        active_field = recovery_page.active_field_password()
        assert active_field != ForgotPasswordPageLocators.PASSWORD_INPUT
