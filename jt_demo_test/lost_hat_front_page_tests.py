import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class LostHatFrontPageTests(unittest.TestCase):
    def setUp(self):
        service = Service('C:\TestFiles\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login?back=my-account'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'

    def tearDown(self):
        self.driver.quit()

    #testy obecności slidera
    def test_slider_exist(self):
        driver = self.driver
        driver.get(self.base_url)
        slider_xpath = "//*[@id='carousel']"
        slider_element = driver.find_element(By.XPATH, slider_xpath)

    # testy rozmiaru slidera
    def test_slider_size(self):
        expected_min_height = 300
        expected_min_width = 600
        slider_xpath = "//*[@id='carousel']"
        driver = self.driver

        driver.get(self.base_url)
        slider_element = driver.find_element(By.XPATH, slider_xpath)
        actual_slider_height = slider_element.size['height']
        actual_slider_width = slider_element.size['width']
        print(actual_slider_height)
        print(actual_slider_width)
        with self.subTest('Element height'):
            self.assertLess(expected_min_height, actual_slider_height,
                        f'Element height found by xpath {slider_xpath} '
                        f'on page {driver.current_url} '
                        f'is smaller than expected {expected_min_height}px')
        with self.subTest('Element width'):
            self.assertLess(expected_min_width, actual_slider_width,
                        f'Element width found by xpath {slider_xpath} '
                        f'on page {driver.current_url} '
                        f'is smaller than expected {expected_min_width}px')

    # testy ilości stron slidera
    def test_slider_contain_exact_number_of_slider(self):
        expected_number_of_sliders = 3
        slider_xpath = "//*[@class='carousel-inner']/li"
        driver = self.driver

        driver.get(self.base_url)
        slider_elements = driver.find_elements(By.XPATH, slider_xpath)
        actual_number_of_sliders = len(slider_elements)
        print(actual_number_of_sliders)
        self.assertEqual(expected_number_of_sliders, actual_number_of_sliders,
                         f'Actual numbers of sliders: {actual_number_of_sliders}, '
                         f'differ than expected {expected_number_of_sliders} '
                         f'on a page {driver.current_url}')

    # testy tekstu na stronach slidera
    def test_sliders_required_title_text(self):
        expected_text_include_in_slider = 'sample'
        slider_title_xpath = "//*[@class='carousel-inner']/li//*[contains(@class, 'text-uppercase')]"
        driver = self.driver

        driver.get(self.base_url)
        title_elements = driver.find_elements(By.XPATH, slider_title_xpath)

        for title_element in title_elements:
            title_elements_text = title_element.get_attribute('textContent')
            title_element_text_lower = title_elements_text.lower()
            print(f'Text: {title_element_text_lower}')
            with self.subTest(title_element_text_lower):
                self.assertIn(expected_text_include_in_slider, title_element_text_lower,
                              f'Actual text of sliders: {title_element_text_lower}, '
                              f'does not include the expected: {expected_text_include_in_slider}, '
                              f'for a page {driver.current_url}')

    # testy ilości produktów na głównej stronie
    def test_right_quantity_of_products_on_main_page(self):
        expected_quantity_of_products = 8
        slider_title_xpath = "//*[@class='product-miniature js-product-miniature']"
        driver = self.driver

        driver.get(self.base_url)
        quantity_of_products = driver.find_elements(By.XPATH, slider_title_xpath)
        actual_quantity_of_products = len(quantity_of_products)
        print(actual_quantity_of_products)
        self.assertEqual(expected_quantity_of_products, actual_quantity_of_products,
                         f'Actual quantity quantity of products on main page: {actual_quantity_of_products}, '
                         f'is differ than expected quantity_of_products_on_main_page: {expected_quantity_of_products}, '
                         f'for page {driver.current_url}')