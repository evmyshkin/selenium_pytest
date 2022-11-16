from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_added_to_cart(self):
        self.should_be_product_name_matching_cart_product_name()
        self.should_be_product_price_matching_cart_product_price()

    def should_be_product_name_matching_cart_product_name(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        product_name_cart_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_ADDED_TO_CART_MESSAGE).text
        assert product_name == product_name_cart_message, "Product name is different from product in the cart"

    def should_be_product_price_matching_cart_product_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        product_price_cart_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_ADDED_TO_CART_MESSAGE).text
        assert product_price == product_price_cart_message, "Product price is different from product in the cart"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is still presented, but should have already disappeared"
