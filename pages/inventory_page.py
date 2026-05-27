from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    BURGER_MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
    
    def click_burger_menu(self):
        self.driver.find_element(*self.BURGER_MENU_BUTTON).click()

    def click_logout(self):

        logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            logout_button
        )
    
    def logout(self):
        self.click_burger_menu()
        self.click_logout()

    def add_all_items_to_cart(self):

        buttons_count = len(
            self.driver.find_elements(
                *self.ADD_TO_CART_BUTTONS
            )
        )

        for expected_count in range(1, buttons_count + 1):

            add_buttons = [
                button for button in self.driver.find_elements(
                    *self.ADD_TO_CART_BUTTONS
                )
                if button.text == "Add to cart"
            ]

            self.driver.execute_script(
                "arguments[0].click();",
                add_buttons[0]
            )

            WebDriverWait(self.driver, 5).until(
                lambda d: int(self.get_cart_badge_count()) >= expected_count
            )
    
    def get_cart_badge_count(self):

        badges = self.driver.find_elements(
            *self.CART_BADGE
        )

        if not badges:
            return "0"

        return badges[0].text

    def get_add_to_cart_buttons_count(self):

        buttons = self.driver.find_elements(
            *self.ADD_TO_CART_BUTTONS
        )

        return len(buttons)
    
    def click_cart(self):
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SHOPPING_CART_LINK)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            cart_link
        )

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("cart.html")
        )
    
    def go_to_cart(self):
        self.click_cart()
