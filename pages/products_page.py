from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class ProductsPage(BasePage):
    PRODUCTS_TITLE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Products")',
    )
    PRODUCT_NAMES = (AppiumBy.ID, "com.androidsample.generalstore:id/productName")
    ADD_TO_CART_BUTTONS = (AppiumBy.ID, "com.androidsample.generalstore:id/productAddCart")
    CART_BUTTON = (AppiumBy.ID, "com.androidsample.generalstore:id/appbar_btn_cart")

    def wait_until_loaded(self):
        self.find(self.PRODUCTS_TITLE)

    def add_first_visible_product_to_cart(self) -> str:
        names = self.find_all(self.PRODUCT_NAMES)
        buttons = self.find_all(self.ADD_TO_CART_BUTTONS)

        if not names or not buttons:
            raise AssertionError("No visible products were available to add to the cart")

        product_name = names[0].text
        buttons[0].click()
        return product_name

    def open_cart(self):
        self.click(self.CART_BUTTON)
