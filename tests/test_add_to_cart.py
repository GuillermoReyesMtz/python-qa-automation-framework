from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_all_items_to_cart(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    expected_count = (
        inventory_page.get_add_to_cart_buttons_count()
    )

    inventory_page.add_all_items_to_cart()

    actual_count = (
        inventory_page.get_cart_item_count()
    )

    assert actual_count == expected_count, f"Expected {expected_count} items in cart, but got {actual_count}"