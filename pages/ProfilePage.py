import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.BasePage import BasePage
from url import URL


class ProfilePage(BasePage):

    def profile_page_url(self):
        return self.driver.get(URL.PROFILE_URL)

    def take_current_url(self):
        return self.current_url

    def click_history_button(self):
        # self.find_element_with_wait(ProfilePageLocators.ORDER_HISTORY)
        self.find_element_to_be_clickable(ProfilePageLocators.ORDER_HISTORY)
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY)
        return self.current_url()
