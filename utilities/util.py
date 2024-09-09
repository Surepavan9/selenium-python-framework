"""
@package utilities

Util class implementation
All most commonly used utilities should be implemented in this class

eg-
    name = self.util.getUniqueName()
"""

import time
import traceback
import random, string
import utilities.custom_logger as cl
import logging


class Util(object):
    log = cl.custom_logger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of the time

        :param sec:
        :param info:
        :return:
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + " ' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type="letters"):
        """
        Get Random strings of characters

        :param length:
        :param type:
        :return:
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        """
        Get a unique name
        :param charCount:
        :return:
        """
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNames(self, listSize=5, itemLength=None):
        """
        Get a list of valid email ids
        :param listSize: Number of name, default is 5 names in a list
        :param itemLength: It should be a list containing number of items equal to the listSize
                            This determines the length of the item in the list -> [1,2,3,4,5]
        :return:
        """
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList

    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string

        :param actualText:
        :param expectedText:
        :return:
        """

        self.log.info("Actual Text From Application web Ui --> :: " + actualText)
        self.log.info("Actual Text From Application web Ui --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def VerifyTextMatch(self, actualText, expectedText):
        """
        Verify Text Match

        :param actualText:
        :param expectedText:
        :return:
        """
        if actualText.lower() == expectedText.lower():
            self.log.info("### VERIFICATION MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches

        Parameters:
            expectedList: Expected List
            actualList: Actual List
            :param expectedList:
            :param actualList:
            :return:
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list

        Parameters:
            expectedList: Expected List
            actualList: Actual List
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True
