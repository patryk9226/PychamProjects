import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class LostHatSmokeTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        service = Service('C:\TestFiles\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.art_url = self.base_url + '9-art'
        self.clothes_url = self.base_url + '3-clothes'
        self.accessories_url = self.base_url + '6-accessories'
        self.login_url = self.base_url + 'login?back=my-account'

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title,
                         f'Expected {expected_title} differ from actual title {actual_title} on page: {url}')

    def test_title_main_page(self):
        url = self.base_url
        expected_title = 'Lost Hat'
        self.assert_title(url, expected_title)

    def test_title_art_page(self):
        url = self.art_url
        expected_title = 'Art'
        self.assert_title(url, expected_title)

    def test_title_clothes_page(self):
        url = self.clothes_url
        expected_title = 'Clothes'
        self.assert_title(url, expected_title)

    def test_title_accessories_page(self):
        url = self.accessories_url
        expected_title = 'Accessories'
        self.assert_title(url, expected_title)

    def test_title_login_page(self):
        url = self.login_url
        expected_title = 'Login'
        self.assert_title(url, expected_title)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()