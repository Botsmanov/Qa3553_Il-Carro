from selenium.webdriver.common.by import By


class LoginPage:

    LOGIN_NAV_LINK = (By.CSS_SELECTOR,"[href = '/login']")
    EMAIL_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.CSS_SELECTOR,"input[name= 'password']")
    LOGIN_BTN=(By.XPATH,"//button[text()='Y’alla!']")
    SUCCESS_MESSAGE = (By.XPATH,"//h3[text()='You are logged in success']")
    OK_BTN = (By.XPATH, "//a[text()='OK']")
    LOG_OUT_BTN =(By.XPATH, "//*[text()='Log out']")
    def  __init__(self,driver):
        self.driver = driver

    def open_login_form(self):
        self.driver.find_element(*self.LOGIN_NAV_LINK).click()

    def fill_email(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password(self,password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def click_ok(self):
        self.driver.find_element(*self.OK_BTN ).click()
