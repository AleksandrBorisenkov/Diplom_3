import allure

from locators.history_page_locators import HistoryPageLocators
from pages.BasePage import BasePage
from url import URL


class HistoryPage(BasePage):

    def history_page_url(self):
        return self.driver.get(URL.HISTORY_URL)

    def click_logout(self):
        self.find_element_with_wait(HistoryPageLocators.LOCATORS_LOGOUT_BUTTON)
        self.click_on_element(HistoryPageLocators.LOCATORS_LOGOUT_BUTTON)