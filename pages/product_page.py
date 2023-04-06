from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):



    def should_be_btn_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BACKET), "Нет кнопки 'Добавить в корзину'"

    def add_to_basket(self):
        btn_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BACKET)
        btn_basket.click()


    def should_be_product_page(self):
        self.should_be_btn_add_to_basket()
        self.should_be_same_name(self.save_product_name())
        self.should_be_price(self.save_price_in_card())

    def save_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_CARD).text
        return product_name

    def should_be_same_name(self, product_name):
        name_in_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MESSAGE)
        text_chk_name = name_in_message.text
        assert product_name == text_chk_name, f"Incorrect product name {text_chk_name}"


    def save_price_in_card(self):
        price_in_card = self.browser.find_element(*ProductPageLocators.PRICE_IN_CARD).text
        return price_in_card

    def should_be_price(self, price_in_card):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE)
        text_price_in_basket = price_in_basket.text
        assert price_in_card == text_price_in_basket, f"Incorrect price in {text_price_in_basket}"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MSG_PRODUCT_ADD_BUSKET), \
            "Success message is presented, but should not be"
    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MSG_PRODUCT_ADD_BUSKET), \
            "Success message is not disappeared, but should be"










