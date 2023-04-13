import unittest

from lost_hat_login_page_tests import LostHatLoginPageTests

def sanit_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(LostHatLoginPageTests('test_login_user'))
    return test_suite

runner = unittest.TextTestRunner(verbosity=1)
runner.run(sanit_suite())
