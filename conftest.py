import pytest

from selenium import webdriver

from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.ProfilePage import ProfilePage
from pages.RecoveryPasswordPage import RecoveryPasswordPage
from url import URL


# настройки инкогнито
@pytest.fixture(scope='function')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--incognito")
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

# @pytest.fixture(scope='function')
# def main_page(driver):
#     page = MainPage(driver)
#     page.get_url(URL.MAIN_URL)
#     return page
#
# @pytest.fixture(scope='function')
# def login_page(driver):
#     page = LoginPage(driver)
#     page.get_url(URL.LOGIN_URL)
#     return page
#
# @pytest.fixture(scope='function')
# def recovery_url(driver):
#     page = RecoveryPasswordPage(driver)
#     page.get_url(URL.RECOVERY_PAS_URL)
#     return page
#
# @pytest.fixture(scope='function')
# def profile_url(driver):
#     page = ProfilePage(driver)
#     page.get_url(URL.PROFILE_URL)
#     return page