import time

from pages.courses.register_course_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        # self.lp.login("test@email.com", "abcabc")
        self.lp.allCourses()
        self.lp.clickAllCourses()
        time.sleep(2)
        self.courses.enterCourseName("javascript for beginners")
        time.sleep(2)
        self.courses.searchCourseName("")
        time.sleep(4)
        self.courses.selectCourseToEnroll("javascript for beginners")
        self.courses.enrollCourse(num="4242424242429899", exp="12/26", cvv="098")
        time.sleep(2)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed")
        # assert True == self.courses.verifyEnrollFailed()
