import time

import pytest
import allure

from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.HistoryPageg import HistoryPage
from pages.ProfilePage import ProfilePage
from url import URL

class TestProfilePage:

    @allure.title('Логинемся, идем в личный кабинет, история заказов, выход из системы')
    def test_login_history_logout(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        history_page = HistoryPage(driver)
        # сверху прогружаем драйверы всех страницы участниц
        # ниже сам тест
        login_page.login_page_open()
        assert login_page.current_url() == URL.LOGIN_URL
        assert 'Вход' in login_page.wait_login_form()
        login_page.fill_login_form('51253@yandex.ru', '12613612')
        main_page.find_and_click_profile_link()
        profile_page.click_history_button()
        assert profile_page.current_url() == URL.HISTORY_URL
        history_page.click_logout()
        assert 'Вход' in login_page.wait_login_form()


