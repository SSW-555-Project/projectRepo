import os
import sys
import unittest
# Add test directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from test.sprint1Test import TestSprint1Func
from test.sprint2Test import TestSprint2Func
from test.sprint3Test import TestSprint3Func

if __name__ == '__main__':



    
    suite = unittest.TestSuite()

    tests = [TestSprint1Func("test_isBirthBeforeDeath"), TestSprint1Func("test_isMarriageBeforeDeath"),TestSprint1Func("test_isDateBeforeCur"),TestSprint1Func("test_isDivorceBeforeDeath")]
    suite.addTests(tests)

    tests = [TestSprint2Func("test_isMaleLastNames"), TestSprint2Func("test_isParentsNotTooOld"),TestSprint2Func("test_US10"),TestSprint2Func("test_US15"), TestSprint2Func("test_Bigamy"),
            TestSprint2Func("test_Sibling_Spacing"), TestSprint2Func("test_us09"), TestSprint2Func("test_us14")]
    suite.addTests(tests)
    
    tests = [TestSprint3Func("test_us20"), TestSprint3Func("test_us24"), TestSprint3Func("test_US22"), TestSprint3Func("test_US23"), TestSprint3Func("test_IsCorrectGender"), TestSprint3Func("test_Is_Marriages_descendants"), TestSprint3Func("test_US18_SiblingsNotMarry"), TestSprint3Func("test_US19_FirstCousinsNotMarry")]    
    suite.addTests(tests)

   

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
