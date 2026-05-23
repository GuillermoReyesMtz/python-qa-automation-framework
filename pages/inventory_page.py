from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    BURGER_MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

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
