import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_csv_data import RegisterCoursesCSVDataTests

# Get all the tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

# Create a test suite combining all the test cases

regressionTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(regressionTest)
