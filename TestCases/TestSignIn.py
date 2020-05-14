import selenium
import unittest
import pytest
from selenium import webdriver
from PageObjects import SignIn


class Login(unittest.TestCase):
    URL = "https://www.amazon.com/"
    email_id = "autoselenium1234@gmail.com"
    password = "Auto1234"
    driver = webdriver.Chrome(executable_path=r"..\\drivers\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.URL)
        cls.driver.maximize_window()
        # cls.driver.find_element_by_link_text().sen

    def testSignIn(self):
        self.driver.implicitly_wait(10)
        sign_in = SignIn.SignInAmazon(self.driver)
        sign_in.ClickOnSignIn()
        sign_in.SetUsername(self.email_id)
        sign_in.ClickOncontinue()
        sign_in.SetPassword(self.password)
        sign_in.ClickOnSignInSubmit()
        print(self.driver.title)
        # self.driver.find_element_by_link_text('New Releases').click()


if __name__ == '__main__':
    unittest.main()
