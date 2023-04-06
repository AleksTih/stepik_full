from .locators import BasketPageLocators
from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):

    def basket_opened_from_main_page(self):
        btn_on_main = self.browser.find_element(*BasePageLocators.BASKET_BTN)
        btn_on_main.click()
    def should_be_cant_see_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items is presented, but should not be"


    def should_be_see_message_basker_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
            "No message 'Your cart is empty Continue shopping'"
