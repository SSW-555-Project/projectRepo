import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import datetime
from func.sprint2Func import *
from func.loadData import readAndSaveToList

def load_data():
    file_name = 'MySample01.ged'
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
        ilist, flist = load_data()

        # test case 01
        for fm in flist:
            self.assertTrue(isParentsNotTooOld(fm, ilist))


    def test_isMaleLastNames(self):
        """Test method isMaleLastNames(familyInfo, indivduallist)"""

        # load data
        ilist, flist = load_data()

        # test case 01
        for fm in flist:
            self.assertTrue(isMaleLastNames(fm, ilist))
    def test_US15(self):
        ilist, flist = load_data()
        for fm in flist:
            self.assertTrue(US15(fm.Children))
    def test_US10(self):
        ilist, flist = load_data()
        for fm in flist:
            cHusband = getItemByID(ilist, fm.HusbandID)
            cWife = getItemByID(ilist, fm.WifeID)
            self.assertTrue(US10(fm.Married,cHusband.Birthday))
            self.assertTrue(US10(fm.Married,cWife.Birthday))    
    #US11:
    def test_US11_Bigamy(self):
        ilist, flist = load_data()
        Bigamy_info = {}
        for fm in flist:
            inf = [fm.Married, fm.Divorced, fm.HusbandID, fm.WifeID]
            Bigamy_info[fm.ID] = inf
        self.assertTrue(US11_noBigamy(Bigamy_info))    
    #US13:
    def test_US13_Sibling_Spacing(self):
        """Test US13_Sibling_Spacing(fm, individualList)"""
        ilist, flist = load_data()
        
        for fm in flist:
            self.assertTrue(US13_Sibling_Spacing(fm, ilist))
    def test_us09(self):
        ilist, flist = load_data()
        
        for fm in flist:
            a,b=US09(fm.HusbandID, fm.WifeID, fm.Children, individualList)
            self.assertTrue(a)
    
    def test_us14(self):
        ilist, flist = load_data()
        
        for fm in flist:
            a,b=US14(fm.Children, fm.ID, individualList)
            self.assertTrue(a)


if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestSprint2Func("test_isParentsNotTooOld")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)