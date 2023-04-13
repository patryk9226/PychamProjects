import unittest
from unittest.loader import makeSuite

from lost_hat_smoke_tests import LostHatSmokeTests

def smok_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(LostHatSmokeTests))
    return test_suite

runner = unittest.TextTestRunner(verbosity=1)
runner.run(smok_suite())
