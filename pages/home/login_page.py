from selenium.webdriver.common.by import By
import time
from pages.home.navigation_page import navigation_Page
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as lg
import logging
from base.basepage import BasePage


class LoginPage(BasePage):
    log = lg.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = navigation_Page(driver)

    # Locators
    _login_link = "SIGN IN"
    _email_Field = "email"
    _password_Field = "login-password"
    _login_button = "login"
    _all_courses = "ALL COURSES"

    def loginButton(self):
        return self.driver.find_element(By.ID, self._login_button)

    def allCourses(self):
        self.log.info(self._all_courses)
        time.sleep(2)
        return self.driver.find_element(By.LINK_TEXT, self._all_courses)

    # actions
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):  # Method argument - email - we are passing it from outside.
        self.sendKeys(email, self._email_Field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_Field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")

    def clickAllCourses(self):
        self.elementClick(self._all_courses, locatorType="link")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(5)

    def verifyLoginSuccess(self):
        result = self.isElementPresent("//*[@class='zc-icon-bell notification-bell']",
                                       locatorType="xpath")
        print("**** verifyLoginSuccess")
        print(result)
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Incorrect login details. Please try again.')]",
                                       locatorType="xpath")
        print("**** verifyLoginFailed")
        print(result)
        time.sleep(10)
        return result

    def verifyTitle(self):
        return self.verifyPageTitle("My Course")

    def logOut(self):
        self.nav.navigateToUserIcon()
        self.elementClick(locator="//a[@href='/logout']", locatorType="xpath")


