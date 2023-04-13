import unittest
from selenium.webdriver.chrome.service import Service
import time
import selenium
from selenium import webdriver

class MainTests(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(self):
        service = Service('C:\TestFiles\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    def test_demo_login(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
        title = driver.title
        print(title)
        assert title == 'Demobank - Bankowość Internetowa - Logowanie'

    def test_demo_accounts(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/konta.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Konta' == title

    def test_demo_desktop(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/pulpit.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Pulpit' == title

    def test_demo_transfer(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/przelew_nowy_zew.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Przelew' == title

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
