from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage


def test_name_is_required(driver):
    home = HomePage(driver)

    home.select_country("Argentina")
    home.select_gender("Female")
    home.tap_lets_shop()

    assert home.read_toast() == "Please enter your name"


def test_user_can_open_product_catalog(driver):
    home = HomePage(driver)
    products = ProductsPage(driver)

    home.enter_store()

    products.wait_until_loaded()


def test_added_product_is_displayed_in_cart(driver):
    home = HomePage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)

    home.enter_store()
    products.wait_until_loaded()

    selected_product = products.add_first_visible_product_to_cart()
    products.open_cart()

    cart.wait_until_loaded()
    assert cart.contains_product(selected_product), (
        f"Expected '{selected_product}' to be displayed in the cart"
    )
