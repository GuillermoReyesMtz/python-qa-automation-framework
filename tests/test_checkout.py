from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_page_two import CheckoutPageTwo
from pages.complete_page import CompletePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkout_process(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    checkout_page_two = CheckoutPageTwo(driver)
    complete_page = CompletePage(driver)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    
    expected_count = (
        inventory_page.get_add_to_cart_buttons_count()
    )

    inventory_page.add_all_items_to_cart()

    actual_count = (
        inventory_page.get_cart_badge_count()
    )

    assert int(actual_count) == expected_count, f"Expected {expected_count} items in cart, but got {actual_count}"

    inventory_page.go_to_cart()

    cart_page.checkout()

    checkout_page.checkout(
        "John",
        "Doe",
        "12345"
    )

    WebDriverWait(driver, 100).until(
        EC.url_contains("checkout-step-two")
        )

    checkout_page_two.finish_checkout()

    assert complete_page.get_complete_header_text() == "Thank you for your order!"