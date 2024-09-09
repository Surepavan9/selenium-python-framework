import time

from pages.courses.register_course_page import RegisterCoursesPage
from pages.home.navigation_page import navigation_Page
from utilities.teststatus import TestStatus
import unittest
import pytest
from pages.home.login_page import LoginPage
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    @pytest.fixture(autouse=True)
    def objectSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)  # Creating object
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = navigation_Page(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/surepavan/PycharmProjects/AutomationFrameWork1_Letskodeit/testdata.csv"))
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
