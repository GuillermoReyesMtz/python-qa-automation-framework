from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    BURGER_MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

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
        add_to_cart_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        for button in add_to_cart_buttons:
            button.click()
    
    def get_cart_item_count(self):

        badge = self.driver.find_element(*self.CART_BADGE)
        return int(badge.text) if badge else 0

    def get_add_to_cart_buttons_count(self):

        buttons = self.driver.find_elements(
            *self.ADD_TO_CART_BUTTONS
        )

        return len(buttons)
