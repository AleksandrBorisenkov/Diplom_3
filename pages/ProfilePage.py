import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.BasePage import BasePage


class ProfilePage(BasePage):

    def click_history_button(self):
        self.find_element_with_wait(ProfilePageLocators.ORDER_HISTORY)
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY)