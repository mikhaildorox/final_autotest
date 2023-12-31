from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_btn_add_to_basket(self):
        click_btn_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        click_btn_basket.click()

    def product_name_should_be_equal_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        # Затем получаем текст элементов для проверки

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        msg_product_name_in_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_IN_BASKET).text
        print(msg_product_name_in_basket)

        assert product_name == msg_product_name_in_basket, "Product name does not match in basket"

    def total_price_should_be_equal_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        # Затем получаем текст элементов для проверки
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_total_price = self.browser.find_element(*ProductPageLocators.MESSAGE_TOTAL_BASKET).text
        print(message_total_price)

        assert product_price == message_total_price, "Product price does not match in basket"
