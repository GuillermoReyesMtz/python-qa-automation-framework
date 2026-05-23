from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    inventory_page.logout()

    WebDriverWait(driver, 10).until(
    EC.url_contains("saucedemo")
)

    assert "inventory" not in driver.current_url
