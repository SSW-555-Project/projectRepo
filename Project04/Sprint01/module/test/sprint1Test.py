import os
import sys
import unittest

# Add test directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# print(os.path.abspath(__file__))

import datetime
from func.sprint1Func import *

class TestSprint1Func(unittest.TestCase):
    """Test mathfuc.py"""

    def test_isBirthBeforeDeath(self):
        """Test method isBirthBeforeDeath(birthDay, deathDay)"""
        
        birthDay = datetime.datetime(1990, 11, 11)
        deathDay = datetime.datetime(2090, 11, 11)
        nowDay = datetime.datetime.now()

        # test case
        self.assertTrue(isBirthBeforeDeath(birthDay, deathDay))
        self.assertTrue(isBirthBeforeDeath(nowDay, deathDay))
        self.assertFalse(isBirthBeforeDeath(deathDay, birthDay))
        self.assertFalse(isBirthBeforeDeath("deathDay", birthDay))
        self.assertFalse(isBirthBeforeDeath(deathDay, "birthDay"))

    def test_isMarriageBeforeDeath(self):
        """Test method isisMarriageBeforeDeath(marriageDay, deathDay)"""

        marriageDay = datetime.datetime(2018, 11, 11)
        deathDay = datetime.datetime(2090, 11, 11)
        nowDay = datetime.datetime.now()

        # test case
        self.assertTrue(isMarriageBeforeDeath(marriageDay, deathDay))
        self.assertFalse(isMarriageBeforeDeath(nowDay, nowDay))
        self.assertFalse(isMarriageBeforeDeath(deathDay, marriageDay))
        self.assertFalse(isMarriageBeforeDeath(123, nowDay))
        self.assertFalse(isMarriageBeforeDeath(nowDay, [123, 45]))


if __name__ == '__main__':
    unittest.main(verbosity=2)

