class SignInAmazon():
    # Locators of elements
    xpath = "//*[@id='nav-signin-tooltip']/a/span"
    textbox_email_id = 'ap_email'
    textbox_password_id = 'ap_password'
    button_continue_id = 'continue'
    button_Sign_In = 'signInSubmit'

    def __init__(self, driver):
        self.driver = driver

    def ClickOnSignIn(self):
        self.driver.find_element_by_xpath(self.xpath).click()

    def SetUsername(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def ClickOncontinue(self):
        self.driver.find_element_by_id(self.button_continue_id).click()

    def SetPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def ClickOnSignInSubmit(self):
        self.driver.find_element_by_id(self.button_Sign_In).click()
