import time

import pytest
import allure

from locators.login_page_locators import LoginPageLocators
from url import URL

class TestProfilePage:

    def test_login_logout(self, login_page, main_page, profile_url):
        url = login_page.current_url()
        assert url == URL.LOGIN_URL
        # time.sleep(1)
        text_form = login_page.wait_login_form()
        assert text_form == 'Вход'
        login_page.fill_login_form('51253@yandex.ru', '12613612')
        main_page.wait_buns()
        # main_page.find_and_click_profile_link()
        # time.sleep(1)
        # check_url = profile_url.click_history_button()
        # assert check_url == URL.HISTORY_URL

