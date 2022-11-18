from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_TOTALS), "Basket totals are presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_MESSAGE), "Empty basket text is missing, but should be presented"
