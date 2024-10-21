import time

import pytest
import allure

from url import URL
from data_help import mail_generator


class TestRecoveryPassword:

    def test_recovery_password_from_login_page(self, recovery_url, login_page):
        login_page.go_to_password_recovery()
        recovery_url.fill_email_recovery(mail_generator())
        time.sleep(1)
        active_field = recovery_url.active_field_password()
        assert active_field == '#4C4CFF'
