from pages.login_page import LoginPage


def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(
        "standard_user",
        "asodifn"
    )

    assert driver.current_url == "https://www.saucedemo.com/"