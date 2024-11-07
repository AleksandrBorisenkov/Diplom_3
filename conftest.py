import pytest

from selenium import webdriver

# настройки инкогнито
@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy='eager'
    options.add_argument("--incognito")
    options.timeouts= { 'pageLoad': 5000 }
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
