import os
import sys
import unittest
# Add test directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from test.sprint1Test import TestSprint1Func
from test.sprint2Test import TestSprint2Func

if __name__ == '__main__':



    
    suite = unittest.TestSuite()

    tests = [TestSprint1Func("test_isBirthBeforeDeath"), TestSprint1Func("test_isMarriageBeforeDeath"),TestSprint1Func("test_isDateBeforeCur"),TestSprint1Func("test_isDivorceBeforeDeath")]
    suite.addTests(tests)

    tests = [TestSprint2Func("test_isMaleLastNames"), TestSprint2Func("test_isParentsNotTooOld"),TestSprint2Func("test_US10"),TestSprint2Func("test_US15"), TestSprint2Func("test_Bigamy"),
            TestSprint2Func("test_Sibling_Spacing")]
    suite.addTests(tests)

   

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
