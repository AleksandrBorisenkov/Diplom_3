import allure

from locators.main_page_locators import MainPageLocators
from pages.BasePage import BasePage
from url import URL


class MainPage(BasePage):

    def main_page_open(self):
        return self.driver.get(URL.MAIN_URL)

    def wait_buns(self):
        self.find_element_with_wait(MainPageLocators.BUNS)

    def find_and_click_profile_link(self):
        # self.full_load_page(MainPageLocators.FULL_LOAD_PAGE)
        self.find_element_to_be_clickable(MainPageLocators.HEADER_PERSONAL_ACCOUNT)
        self.click_on_element(MainPageLocators.HEADER_PERSONAL_ACCOUNT)

    def click_enter_account(self):
        self.find_elements_with_wait(MainPageLocators.BUTTON_ENTER_ACCOUNT)
        self.click_on_element(MainPageLocators.BUTTON_ENTER_ACCOUNT)

    def click_create_order(self):
        self.find_element_with_wait(MainPageLocators.CREATE_ORDER)
        self.click_on_element(MainPageLocators.CREATE_ORDER)

    def click_on_ingredients(self):
        self.find_element_with_wait(MainPageLocators.BUN1_INFO)
        self.click_on_element(MainPageLocators.BUN1_INFO)
        element = self.get_text_from_element(MainPageLocators.INGREDIENT_INFO)
        return element

    def close_info_ingredients(self):
        self.click_on_ingredients()
        self.click_on_element(MainPageLocators.INGREDIENT_INFO_CLOSE_BUTTON)


