from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BACKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME_IN_CARD = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_IN_CARD = (By.CSS_SELECTOR, "p.price_color")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")
    MSG_PRODUCT_ADD_BUSKET = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, "span a.btn.btn-default")
    BASKET_BTN_INVALID = (By.CSS_SELECTOR, "btn_inc")

class BasketPageLocators():
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")