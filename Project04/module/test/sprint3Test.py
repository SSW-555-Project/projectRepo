import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import datetime
from func.sprint2Func import *
from func.sprint3Func import *

from func.loadData import readAndSaveToList

def load_data():
    file_name = 'userStory.ged'
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


class TestSprint3Func(unittest.TestCase):
    """Test mathfuc.py"""
            
    def test_us20(self):
        ilist, flist = load_data()
        for fm in flist:
            us20a,us20b=US20(fm.WifeID, fm.HusbandID, flist)
            self.assertTrue(us20a)
            
    def test_us24(self):
        ilist, flist = load_data()
        for fm in flist:
            us24a, us24b =US24(fm.WifeName, fm.HusbandName, fm.Married, fm.ID, flist)
            self.assertTrue(us24a)
         
    def test_US22(self):
        ilist, flist = load_data()
        IDset=set()
        for pp in ilist:
            result=US22(IDset,pp.ID)
            self.assertTrue(result)
        for fm in flist:
            result=US22(IDset,fm.ID)
            self.assertTrue(result)
    def test_US23(self):
        ilist, flist = load_data()
        individualDict=dict()
        for pp in ilist:
            result=US23(individualDict,pp.ID,pp.Birthday)
            self.assertTrue(result)
    def test_IsCorrectGender(self):
        """Test method IsCorrectGender(wID, hID, individualList)"""
        
        # load data
        ilist, flist = load_data()

        # test case 01
        for fm in flist:
            result, msg = IsCorrectGender(fm.WifeID,fm.HusbandID, ilist)
            self.assertTrue(result)

        # test case 02
        ilist[0].Gender = 'F'
        ilist[1].Gender = 'M'
        result, msg = IsCorrectGender(flist[0].WifeID,flist[0].HusbandID, ilist)
        self.assertFalse(result)

    def test_Is_Marriages_descendants(self):
        """Test method Is_Marriages_descendants(familyList)"""

        # load data
        ilist, flist = load_data()

        # test case 01
        self.assertTrue(Is_Marriages_descendants(flist))

        # test case 02
        flist[0].WifeID = "I3"
        result, msg = Is_Marriages_descendants(flist)
        self.assertFalse(result)
        
    def test_US18_SiblingsNotMarry(self):
        ilist, flist = load_data()
        for fm in flist:
            self.assertTrue(US18_SiblingsNotMarry(fm, flist, ilist))
    
    def test_US19_FirstCousinsNotMarry(self):
        ilist, flist = load_data()
        for fm in flist:
            self.assertTrue(US19_FirstCousinsNotMarry(fm, flist, ilist))
        
if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestSprint3Func("test_us20"),TestSprint3Func("test_us24"),TestSprint3Func("test_US22"),TestSprint3Func("test_US23")]
    suite.addTests(tests)

    tests = [TestSprint3Func("test_IsCorrectGender"),TestSprint3Func("test_Is_Marriages_descendants")]
    suite.addTests(tests)
    
    tests = [TestSprint3Func("test_US18_SiblingsNotMarry"),TestSprint3Func("test_US19_FirstCousinsNotMarry")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)