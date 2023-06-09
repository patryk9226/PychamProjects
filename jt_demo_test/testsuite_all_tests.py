import unittest

from lost_hat_smoke_tests import LostHatSmokeTests
from lost_hat_front_page_tests import LostHatFrontPageTests
from lost_hat_login_page_tests import LostHatLoginPageTests
from lost_hat_product_page_tests import LostHatProductPageTests

def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(LostHatSmokeTests))
    test_suite.addTest(unittest.makeSuite(LostHatFrontPageTests))
    test_suite.addTest(unittest.makeSuite(LostHatLoginPageTests))
    test_suite.addTest(unittest.makeSuite(LostHatProductPageTests))
    return test_suite

runner = unittest.TextTestRunner(verbosity=2)
runner.run(full_suite())