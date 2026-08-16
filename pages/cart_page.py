from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_TITLE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Cart")',
    )
    PRODUCT_NAMES = (AppiumBy.ID, "com.androidsample.generalstore:id/productName")
    TOTAL_AMOUNT = (AppiumBy.ID, "com.androidsample.generalstore:id/totalAmountLbl")

    def wait_until_loaded(self):
        self.find(self.CART_TITLE)

    def product_names(self) -> list[str]:
        return [element.text for element in self.find_all(self.PRODUCT_NAMES)]

    def contains_product(self, product_name: str) -> bool:
        return product_name in self.product_names()
