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
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        title = driver.title
        print('Actual title (format()): {}'.format(title))
        # assert title == 'Demobank - Bankowość Internetowa - Logowanie'
        self.assertEqual('Demobank - Bankowość Internetowa - Logowanie', title,
                         f'Expected title differ from actual for page url: {url}')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
