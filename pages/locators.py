from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_ADDED_TO_CART_MESSAGE = (
        By.CSS_SELECTOR, "#messages :first-child .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .price_color")
    PRODUCT_PRICE_ADDED_TO_CART_MESSAGE = (
        By.CSS_SELECTOR, "#messages > :last-child strong")
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR, "#messages > :nth-child(1) > .alertinner")
    
class BasketPageLocators():
    BASKET_TOTALS = (By.CSS_SELECTOR, "#basket_totals")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
