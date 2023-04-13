import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from helpers import functional_helpers as fh
from helpers import assertion_helpers as ah


class LostHatLoginPageTests(unittest.TestCase):
    def setUp(self):
        service = Service('C:\TestFiles\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login?back=my-account'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'

    def tearDown(self):
        self.driver.quit()

    #test poprawnej strony logowania
    def test_header_on_login_page(self):
        driver = self.driver
        driver.get(self.login_url)
        xpath = "//*[@class='page-header']/h1"
        expected_text = 'Log in to your account'

        #użycie metody do sprawdznie textu
        ah.assert_element_text(self, driver, xpath, expected_text)

    #test logowania usera
    def test_login_user(self):
        driver = self.driver
        driver.get(self.login_url)
        user_email = 'patryknowak9226@gmail.com'
        user_pass = 'autodemopn'
        expected_text = 'Your account'
        xpath = "//*[@class='page-header']/h1"


        #użycie metody do zalogowania
        fh.user_login(driver, user_email, user_pass)

        #użycie metody do sprawdznie textu
        ah.assert_element_text(self, driver, xpath, expected_text)

    #test błędnego logowania usera
    def test_not_login_user(self):
        driver = self.driver
        driver.get(self.login_url)
        user_email = 'invalid@gmail.com'
        user_pass = 'invalidpass'
        expected_text = 'Authentication failed.'
        xpath = "//*[@class='alert alert-danger']"

        #użycie metody do zalogowania
        fh.user_login(driver, user_email, user_pass)

        #użycie metody do sprawdznie textu
        ah.assert_element_text(self, driver, xpath, expected_text)