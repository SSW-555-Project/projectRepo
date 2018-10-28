import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import datetime
from func.sprint2Func import *
from func.sprint3Func import *

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


class TestSprint3Func(unittest.TestCase):
    """Test mathfuc.py"""
            
    def test_us20(self):
        ilist, flist = load_data()
        for fm in flist:
            us20a,us20b=US20(fm.WifeID, fm.HusbandID, flist)
            self.assertTrue(a)
            
    def test_us24(self):
        ilist, flist = load_data()
        for fm in flist:
            us24a, us24b =US24(fm.WifeName, fm.HusbandName, fm.Married, fm.ID, flist)
            self.assertTrue(a)
            
            
            

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestSprint3Func("test_us20"),TestSprint3Func("test_us24")]
    
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)