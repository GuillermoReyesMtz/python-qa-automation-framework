from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        self.driver.execute_script(
            "arguments[0].click();",
            checkout_button
        )

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-one.html")
        )

    def checkout(self):
        self.click_checkout()

