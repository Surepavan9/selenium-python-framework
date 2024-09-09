from selenium.webdriver.common.by import By
import time
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as lg
import logging
from base.basepage import BasePage


class navigation_Page(BasePage):
    log = lg.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _home = "HOME"
    _all_courses = "ALL COURSES"
    _interview = "INTERVIEW"
    _support = "SUPPORT"
    _blog = "BLOG"
    _practice = "PRACTICE"
    _myCourses = "MY COURSES"
    _community = "COMMUNITY"
    _user_settings_icon = "//*[@class='btn btn-sm dropdown-toggle zl-navbar-rhs-btn']"

    def navigateToHome(self):
        self.elementClick(locator=self._home, locatorType="link")

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToInterview(self):
        self.elementClick(locator=self._interview, locatorType="link")

    def navigateToSupport(self):
        self.elementClick(locator=self._support, locatorType="link")

    def navigateToBlog(self):
        self.elementClick(locator=self._blog, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._myCourses, locatorType="link")

    def navigateToMyCommunity(self):
        self.elementClick(locator=self._community, locatorType="link")

    def navigateToUserIcon(self):
        self.elementClick(locator=self._user_settings_icon, locatorType="xpath")
