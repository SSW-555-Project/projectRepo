
# coding: utf-8

# In[ ]:


import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import datetime
from func.sprint4Func import *
from func.loadData import readAndSaveToList

def load_data():
    file_name = 'nov10.ged'
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

class TestSprint4Func(unittest.TestCase):
    """Test mathfuc.py"""
            
    def test_US38_upcomingBirthdays(self):
        ilist, flist = load_data()
        for indi in ilist:
            if indi.ID == "I10":
                self.assertTrue(US38_upcomingBirthdays(indi))
    def test_US39_upcomingAnniversaries(self):
        ilist, flist = load_data()
        for fm in flist:
            if fm.ID == "F3":
                self.assertTrue(US39_upcomingAnniversaries(fm))
                
    def test_us29(self):
        ilist, flist = load_data()
        for pp in ilist:
            if US29(pp.ID, pp.Name ,pp.Alive)!=None:
                 self.assertTrue(US29(pp.ID, pp.Name ,pp.Alive))
    
    def test_us30(self):
        ilist, flist = load_data()
        for fm in flist:
            if US30(fm.ID, fm.Divorced, fm.HusbandID, fm.WifeID,ilist)!=None:
                self.assertTrue(US30(fm.ID, fm.Divorced, fm.HusbandID, fm.WifeID,ilist))

    def test_ListMultipleBirths(self):
        ilist, flist = load_data()

        tp = ListMultipleBirths(ilist)
         
        self.assertEqual(len(tp), 8)

    def test_ListLivingSingle(self):

        ilist, flist = load_data()

        tp = ListLivingSingle(ilist)

        self.assertEqual(len(tp), 0)          
            
if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestSprint4Func("test_US38_upcomingBirthdays"),TestSprint4Func("test_US39_upcomingAnniversaries"),\
            TestSprint4Func("test_us29"),TestSprint4Func("test_us30")]
    
    suite.addTests(tests)
    

    tests = [TestSprint4Func("test_ListMultipleBirths"),TestSprint4Func("test_ListLivingSingle")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

