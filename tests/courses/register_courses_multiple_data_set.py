import time

from pages.courses.register_course_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from pages.home.login_page import LoginPage
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("test@email.com", "abcabc", "javascript for beginners", "javascript for beginners", "4242424242429899",
           "12/26", "098"),("test@email.com", "abcabc", "Learn Python 3 from scratch", "Learn Python 3 from scratch",
                            "4242424242424243", "11/29", "123"))  # tuples or list
    @unpack
    def test_invalidEnrollment(self, email, password, name, fullCourseName, num, exp, cvv):
        self.lp.login(email, password)
        self.lp.allCourses()
        self.lp.clickAllCourses()
        time.sleep(2)
        self.courses.enterCourseName(name)
        time.sleep(2)
        self.courses.searchCourseName("")
        time.sleep(4)
        self.courses.selectCourseToEnroll(fullCourseName)
        self.courses.enrollCourse(num, exp, cvv)
        time.sleep(2)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed")
        # self.driver.find.element_by_link_text("All Courses").click()
        self.driver.get('https://www.letskodeit.com/mycourses')
        # assert True == self.courses.verifyEnrollFailed()
