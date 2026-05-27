from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class CheckoutPage:

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        field = self.driver.find_element(*self.FIRST_NAME_INPUT)
        field.clear()
        field.send_keys(first_name)
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*self.FIRST_NAME_INPUT).get_attribute("value") == first_name
        )

    def enter_last_name(self, last_name):
        field = self.driver.find_element(*self.LAST_NAME_INPUT)
        field.clear()

        ActionChains(self.driver)\
        .click(field)\
        .send_keys(last_name)\
        .perform()
        
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*self.LAST_NAME_INPUT).get_attribute("value") == last_name
        )
    
    def enter_postal_code(self, postal_code):
        field = self.driver.find_element(*self.POSTAL_CODE_INPUT)
        field.clear()
        field.send_keys(postal_code)
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*self.POSTAL_CODE_INPUT).get_attribute("value") == postal_code
        )

    def click_continue(self):

        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )

        self.driver.save_screenshot("continue_debug.png")

        print(
        self.driver.find_element(
            *self.FIRST_NAME_INPUT
        ).get_attribute("value")
        )

        print(
            self.driver.find_element(
                *self.LAST_NAME_INPUT
            ).get_attribute("value")
        )

        print(
            self.driver.find_element(
                *self.POSTAL_CODE_INPUT
            ).get_attribute("value")
        )

        self.driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-two")
        )
    
    def checkout(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()