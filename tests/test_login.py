from pages.login_page import LoginPage
import time

Valid_Email = "rahant@gmail.com"
Valid_Password = "Talito@96"

def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    time.sleep(2)
    login_page.fill_email(Valid_Email)
    login_page.fill_password(Valid_Password)
    login_page.submit_login()
    time.sleep(2)
    login_page.click_ok()


