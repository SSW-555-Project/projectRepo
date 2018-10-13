import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import datetime
from func.sprint2Func import *
from func.loadData import readAndSaveToList

def load_data(file_name):

    # create list for individual and families
    ilist = []
    flist = []

    # input sample
    filePath = os.path.join(os.getcwd(), "Sample/" + file_name)

    # read file to create individual and families
    if os.path.exists(filePath):
        readAndSaveToList(filePath, ilist, flist)
    else:
        print("File doesn't exist")

    return ilist, flist


class TestSprint2Func(unittest.TestCase):
    """Test mathfuc.py"""

    def test_isParentsNotTooOld(self):
        """Test method isParentsNotTooOld(familyInfo, indivduallist)"""
        
        # load data
        ilist, flist = load_data('UserStory.ged')

        # test case 01
        for fm in flist:
            self.assertTrue(isParentsNotTooOld(fm, ilist))


    def test_isMaleLastNames(self):
        """Test method isMaleLastNames(familyInfo, indivduallist)"""

        # load data
        ilist, flist = load_data('UserStory.ged')

        # test case 01
        for fm in flist:
            self.assertTrue(isMaleLastNames(fm, ilist))
    def test_US10(self):
        ilist, flist = load_data('UserStory.ged')
        for fm in flist:
            cHusband = getItemByID(ilist, fInfo.HusbandID)
            cWife = getItemByID(ilist, fInfo.WifeID)
            self.assertTrue(US10(fm.Married,cHusband.Birthday)
            self.assertTrue(US10(fm.Married,cWife.Birthday)                
    def test_US15(self):
        ilist, flist = load_data('UserStory.ged')
        for fm in flist:
            self.assertTrue(US15(fm.Children))


if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestSprint2Func("test_isParentsNotTooOld")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

