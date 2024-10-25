import time

import pytest
import allure

from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.ProfilePage import ProfilePage
from url import URL

class TestProfilePage:

    def test_login_logout(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        login_page.login_page_open()
        url = login_page.current_url()
        assert url == URL.LOGIN_URL
        text_form = login_page.wait_login_form()
        assert text_form == 'Вход'
        login_page.fill_login_form('51253@yandex.ru', '12613612')
        main_page.wait_buns()
        main_page.find_and_click_profile_link()
        # time.sleep(1)
        check_url= profile_page.click_history_button()
        # time.sleep(1)
        # check_url = profile_page.current_url()
        assert check_url == URL.HISTORY_URL

