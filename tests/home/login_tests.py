import time
from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        time.sleep(2)

        result1 = self.lp.verifyTitle()

        assert result1 == True

        self.ts.mark(result1, "Titles is incorrect")

        result2 = self.lp.verifyLoginSuccess()
        assert result2 == True
        self.ts.markFinal("test_validLogin", result2, "Login wasn't successful")


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logOut()
        self.lp.login("test@email.com", "abcabcd")
        result2 = self.lp.verifyLoginFailed()
        time.sleep(6)
        assert result2 == True
        self.ts.mark( None, "invalid login")
