import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class RegisterCoursesPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    # _Search_box = "search"  # //input[@id='search']
    _Search_box = "//input[@id='search']"
    _course = "//*[@class='dynamic-heading']"
    _all_courses = "ALL COURSES"
    _search_button = "//button[@type='submit']"
    _enroll_button = "//*[@class='dynamic-button btn btn-default btn-lg btn-enroll']"
    _paymentFrame_click = "//*[contains(text(), 'Payment Information')]"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "exp-date"  # "//input[@name='exp-date' and @placeholder='MM / YY']"
    _cc_cvv = "cvc"  # "//*[@name='cvc' and @placeholder='Security Code']"
    _submit_enroll = "//*[@class='dynamic-button btn btn-default btn-lg btn-enroll']" # //*[@class='checkbox margin-top-10 margin-bottom-10 jqGdprCheckbox']
    _enroll_error_message = "//div[contains[@class,'error-message') and contains(text(), 'Your card number is invalid.']"  # //div[@class='alert alert-danger']

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._Search_box, locatorType="xpath")

    def searchCourseName(self, search):
        self.elementClick(locator=self._search_button, locatorType="xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")
        # self.elementClick(fullCourseName, self._course)

    def enterCardNum(self, num):
        # This frame takes at least 6 seconds to show, it may take more of you
        time.sleep(8)
        # self.switchToFrame(name="__privateStripeFrame3793")  # Here we are switching to iframe
        self.SwitchFrameByIndex(self._cc_num,locatorType="xpath")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        # self.switchToFrame(name="__privateStripeFrame3795")
        self.SwitchFrameByIndex(self._cc_exp, locatorType="name")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        # self.switchToFrame(name="cardExpiryButton3797")
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="name")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(self._enroll_button, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickEnrollSubmitButton()
        self.webScroll(direction="down")  # self.driver.execute_script("window.scrollBy(0, 800);")  #
        self.enterCreditCardInformation(num, exp, cvv)
        time.sleep(5)
        self.clickEnrollSubmitButton()
        time.sleep(5)

    def verifyEnrollFailed(self):
        result = self.isElementPresent(self._enroll_error_message, locatorType="xpath")
        # "//input[contains(@id, 'search') and contains(@placeholder, 'Search Course')]")
        time.sleep(5)
        print("**** verifyEnrollFailed***")
        print(result)
        return result
