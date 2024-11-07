import allure

from pages.LoginPage import LoginPage
from pages.RecoveryPasswordPage import RecoveryPasswordPage
from data_help import mail_generator


@allure.description('Заходим на страницу логина и переходим на сброс пароля')
class TestRecoveryPassword:

    @allure.title('Переход на страницу сброса пароля и проверяем, что поле пароль подсвечено если нажать глазик')
    def test_recovery_password_from_login_page(self, driver):
        login_page = LoginPage(driver)
        recovery_page = RecoveryPasswordPage(driver)
        # сверху прогружаем драйверы всех страницы участниц
        # ниже сам тест
        login_page.login_page_open()
        login_page.go_to_password_recovery()
        recovery_page.fill_email_recovery(mail_generator())
        active_field = recovery_page.active_field_password()
        assert active_field != recovery_page.active_field_or_not
