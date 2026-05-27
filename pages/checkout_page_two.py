from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPageTwo:

    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def click_finish(self):
        finish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )
        self.driver.execute_script(
            "arguments[0].click();",
            finish_button
        )

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-complete.html")
        )
    
    def finish_checkout(self):
        self.click_finish()
    
