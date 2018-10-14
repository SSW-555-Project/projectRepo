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
    filePath = file_name

    # read file to create individual and families
    if os.path.exists(filePath):
        readAndSaveToList(filePath, ilist, flist)
    else:
        print("File doesn't exist")

    return ilist, flist


class TestSprint2Func(unittest.TestCase):
    def test_US15(self):
        ilist,flist=load_data('userStory.ged')
        for fm in flist:
            self.assertTrue(US15(fm.Children))
    def test_US10(self):
        ilist, flist = load_data('userStory.ged')
        for fm in flist:
            cHusband = getItemByID(ilist, fInfo.HusbandID)
            cWife = getItemByID(ilist, fInfo.WifeID)
            self.assertTrue(US10(fm.Married,cHusband.Birthday)
                           


if __name__ == '__main__':
    unittest.main() 


