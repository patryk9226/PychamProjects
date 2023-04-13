import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from helpers import assertion_helpers as ah


class LostHatProductPageTests(unittest.TestCase):
    def setUp(self):
        service = Service('C:\TestFiles\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login?back=my-account'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'

    def tearDown(self):
        self.driver.quit()

    #test nazwy produktu
    def test_product_name(self):
        driver = self.driver
        driver.get(self.sample_product_url)
        expected_text = 'HUMMINGBIRD PRINTED T-SHIRT'
        xpath = "//*[@itemprop='name' and @class='h1']"

        #użycie metody do sprawdznie textu
        ah.assert_element_text(self, driver, xpath, expected_text)

    #test ceny produktu
    def test_product_price(self):
        driver = self.driver
        driver.get(self.sample_product_url)
        expected_text = 'PLN23.52'
        xpath = "//*[@itemprop='price']"

        #użycie metody do sprawdznie textu
        ah.assert_element_text(self, driver, xpath, expected_text)