import allure

from data_help import exist_user_email, exist_user_password
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.HistoryPage import HistoryPage
from pages.ProfilePage import ProfilePage


@allure.description('Логинемся и идем в личный кабинет и выходим от туда.')
class TestProfilePage:

    @allure.title('Логинемся, идем в личный кабинет, в историю заказов и выход из системы.')
    def test_login_history_logout(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        history_page = HistoryPage(driver)
        # сверху прогружаем драйверы всех страницы участниц
        # ниже сам тест
        login_page.login_page_open()
        login_page.fill_login_form(exist_user_email, exist_user_password)
        main_page.find_and_click_profile_link()
        profile_page.click_history_button()
        history_page.click_logout()
        assert 'Вход' in login_page.wait_login_form()
