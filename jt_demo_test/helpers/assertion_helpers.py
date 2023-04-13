from selenium.webdriver.common.by import By

def assert_element_text(test_self, driver, xpath, expected_text):
    """Comparing expected text with observed value from web element

     :param driver: webdriver instance
     :param xpath: xpath to element with text to be observed
     :param expected_text: text what we expecting to be found
     :return: None
    """
    element = driver.find_element(By.XPATH, xpath)
    element_text = element.text
    print(f'Text of element: {element_text}')
    test_self.assertEqual(expected_text, element_text, f'Expected text differ from actual on page: {driver.current_url}')