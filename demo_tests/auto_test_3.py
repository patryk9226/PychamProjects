import unittest
from selenium.webdriver.chrome.service import Service
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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

    def test_demo_accounts(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/konta.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title (f {{}}): {title}')
        # assert 'Demobank - Bankowość Internetowa - Konta' == title
        self.assertEqual('Demobank - Bankowość Internetowa - Konta', title,
                         f'Expected title differ from actual for page url: {url}')

    def test_demo_desktop(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/pulpit.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title (+): ' + title)
        # assert 'Demobank - Bankowość Internetowa - Pulpit' == title
        self.assertEqual('Demobank - Bankowość Internetowa - Pulpit', title,
                         f'Expected title differ from actual for page url: {url}')

    def test_demo_transfer(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/przelew_nowy_zew.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title (procent s): %s' % (title))
        # assert 'Demobank - Bankowość Internetowa - Przelew' == title
        self.assertEqual('Demobank - Bankowość Internetowa - Przelew', title,
                         f'Expected title differ from actual for page url: {url}')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

class LoginPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        service = Service('C:\TestFiles\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


    def test_header_of_main_page(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        # sprawdzenie i porównnie nagłówka srony logowania z wzorcowym
        header_of_main_page = driver.find_element(By.XPATH, "//*[@id='header_1']")
        header_of_main_page_text = header_of_main_page.text
        self.assertEqual('Wersja demonstracyjna serwisu demobank', header_of_main_page_text, f'Expected head of main page: {url}')
        print(f'Header of main page : {header_of_main_page_text}')

    def test_button_next_active(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        #sprawdzenie stanu przycisku "dalej" na początku testu
        button_next = driver.find_element(By.XPATH, "//*[@id='login_next']")
        button_next_disabled = button_next.get_property('disabled')
        print(f'Button next disabled value: {button_next_disabled}')
        self.assertEqual(True, button_next_disabled,
                         f'Expected state of "dalej" button: True , differ from actual: {button_next_disabled} , for page url: {url}')

        time.sleep(2)

        #wpisanie do okineka logowania 8 znaków
        login_input_element = driver.find_element(By.XPATH, "//*[@id='login_id']")
        login_input_element_before_text = login_input_element.get_attribute('value')
        print(f'Login input element: {login_input_element_before_text}')
        login_input_element.send_keys('12345678')
        login_input_element_after_text = login_input_element.get_attribute('value')
        print(f'Login input element: {login_input_element_after_text}')

        time.sleep(2)

        #sprawdzenie stanu przycisku "dalej" po wpisaniu 8 znaków
        button_next_after = driver.find_element(By.XPATH, "//*[@id='login_next']")
        button_next_disabled_after = button_next_after.get_property('disabled')
        print(f'Button next disabled after value: {button_next_disabled_after}')
        self.assertEqual(False, button_next_disabled_after, f'Expected state of "dalej" button: False , differ from actual: {button_next_disabled_after} , for page url: {url}')

        #czyszczenia okienka logowania
        login_input_element_to_clear = driver.find_element(By.XPATH, "//*[@id='login_id']")
        login_input_element.clear()
        login_input_element_after_clear = login_input_element_to_clear.get_attribute('value')
        print(f'Login input element after clear: {login_input_element_after_clear}')

        # sprawdzenie stanu przycisku "dalej" po wyczyszczeniu okinka logowania
        button_next_after_clear = driver.find_element(By.XPATH, "//*[@id='login_next']")
        button_next_disabled_after_clear = button_next_after_clear.get_property('disabled')
        print(f'Button next disabled after value: {button_next_disabled_after_clear}')
        self.assertEqual(True, button_next_disabled_after_clear,
                         f'Expected state of "dalej" button: False , differ from actual: {button_next_disabled_after_clear} , for page url: {url}')

        time.sleep(2)

    def test_less_than_8_characters(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        #czyszczenie okienka logowania
        login_input_element = driver.find_element(By.XPATH, "//*[@id='login_id']")
        print(f'Login input element after clear: {login_input_element.clear()}')

        time.sleep(1)

        #wpisanie do okineka logowania mniej niż 8 znaków
        login_input_element = driver.find_element(By.XPATH, "//*[@id='login_id']")
        login_input_element.send_keys('1234567')

        #sprawdzenie co jest wisane w okinko
        login_input_element = driver.find_element(By.XPATH, "//*[@id='login_id']")
        login_input_element_less_than_8_characters = login_input_element.get_attribute('value')
        print(f'Login input element with less than 8 characters: {login_input_element_less_than_8_characters}')

        time.sleep(1)

        #kliknięcie na przycisk pytajnika
        #aby zrobić clica trzeba szukać jednego elementu a nie elements
        question_mark_element = driver.find_element(By.XPATH, "//*[@id='login_id_container']//*[@class='i-hint-white tooltip widget-info']")
        question_mark_element.click()

        #policzenie ile obiektów jest na stronie z danym adresem xpath musi być elements
        quantity_of_elements = len(driver.find_elements(By.XPATH, "//*[@class='i-hint-white tooltip widget-info']"))
        print(f'Quantity of elements: {quantity_of_elements}')


        time.sleep(1)

        #pobranie wartości errora
        error_element = driver.find_element(By.XPATH, "//*[@id='error_login_id']")
        #error_element_textContent = error_element.get_attribute('textContent')
        print(f'Login input element with less than 8 characters: {error_element.text}')

        #sprawdzenie czy zgadza się error
        self.assertEqual('identyfikator ma min. 8 znaków', error_element.text, f'Expected warning message differ from actual one for url: {url}')

    def test_skip_to_login_stage_2(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        #czyszczenie okienka logowania
        login_input_element = driver.find_element(By.XPATH, "//*[@id='login_id']")
        login_input_element.clear()
        login_input_element_after_clear = login_input_element.get_attribute('value')
        print(f'Login input element after clear: {login_input_element_after_clear}')

        time.sleep(1)

        #wpisanie do okineka logowania 8 znaków
        login_input_element = driver.find_element(By.XPATH, "//*[@id='login_id']")
        login_input_element.send_keys('12345678')

        #sprawdzenie co jest wisane w okinko
        login_input_element = driver.find_element(By.XPATH, "//*[@id='login_id']")
        login_input_element_8_characters = login_input_element.get_attribute('value')
        print(f'Login input element with less than 8 characters: {login_input_element_8_characters}')

        #wciśnięcie przycisku dalej
        button_next = driver.find_element(By.XPATH, "//*[@id='login_next']")
        button_next.click()

        time.sleep(1)

        #znalezieni obiektu zaloguj się
        login_button_element = driver.find_element(By.XPATH, "//*[@type='submit']")
        login_button_element_textContent = login_button_element.get_attribute('textContent')
        print(f'Name button to login user: {login_button_element_textContent}')
        self.assertEqual('zaloguj się', login_button_element_textContent,
                         f'Expected login button text: zaloguj się , differ from actual {login_button_element_textContent}')

    def test_right_text_after_use_reminder_id(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        #znalezienie tekstu przypomnij identyfikator i kliknięcie w niego
        reminder_id = driver.find_element(By.XPATH, "//*[@id='ident_rem']")
        reminder_id.click()

        time.sleep(1)

        #znalezienie i odczytanie tekstu powiadominie
        reminder_id_monit_text = driver.find_element(By.XPATH, "//*[@class='shadowbox-content contact-popup']/div/h2")
        reminder_id_monit_text_outerText = reminder_id_monit_text.get_attribute('outerText')
        print(f'Monit after use reminder button: {reminder_id_monit_text_outerText}')

        #sprawdzenie tekstu powiadominie
        self.assertEqual('ta funkcja jest niedostępna', reminder_id_monit_text_outerText, f'Expected monit reminder button text: ta funkcja jest niedostępna , differ from actual {reminder_id_monit_text_outerText}')

        time.sleep(1)

        #zamknięcie okna z monitem
        reminder_id_monit_text_x_button = driver.find_element(By.XPATH, "//*[@class='shadowbox-close']")
        reminder_id_monit_text_x_button.click()

        time.sleep(1)

    def test_login_to_the_stage_3(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_2.html?login'
        driver.get(url)

        time.sleep(1)

        ##znalezienie wpisanie i sprawdznie identyfikatora

        # czyszczenie okienka logowania
        login_input_element = driver.find_element(By.XPATH, "//*[@id='login_id']")
        login_input_element.clear()
        login_input_element_after_clear = login_input_element.get_attribute('value')
        print(f'Login input element after clear: {login_input_element_after_clear}')

        #wpisanie do okineka logowania 8 znaków
        login_input_element = driver.find_element(By.XPATH, "//*[@id='login_id']")
        login_input_element.send_keys('12345678')

        time.sleep(3)

        #sprawdzenie co jest wisane w okinku logowania
        login_input_element = driver.find_element(By.XPATH, "//*[@id='login_id']")
        login_input_element_8_characters = login_input_element.get_attribute('value')
        print(f'Login input element with less than 8 characters: {login_input_element_8_characters}')

        ##znalezienie wpisanie i sprawdznie hasła

        # czyszczenie okienka hasła
        password_input_element = driver.find_element(By.XPATH, "//*[@id='login_password']")
        password_input_element.clear()
        password_input_element_after_clear = password_input_element.get_attribute('value')
        print(f'Password input element after clear: {password_input_element_after_clear}')

        #wpisanie do okineka hasła 8 znaków
        password_input_element = driver.find_element(By.XPATH, "//*[@id='login_password']")
        password_input_element.send_keys('abcdefgh')

        time.sleep(3)

        #sprawdzenie co jest wisane w okinku hasła
        password_input_element = driver.find_element(By.XPATH, "//*[@id='login_password']")
        password_input_element_8_characters = password_input_element.get_attribute('value')
        print(f'Password input element with less than 8 characters: {password_input_element_8_characters}')

        #kliknięcie przycisku zaloguj się
        login_button_element = driver.find_element(By.XPATH, "//*[@type='submit']")
        login_button_element.click()

        time.sleep(3)

        #sprawdzneie zalogowania, test tekstu Konto osobiste
        check_site_open = driver.find_element(By.XPATH, "//*[@id='main_content']/*[@class='grid dashboard-section']/*[@class='wborder']")
        check_site_open_outerText = check_site_open.get_attribute('outerText')
        print(f'Login input element with less than 8 characters: {check_site_open_outerText}')

        #test zalogowanie
        self.assertEqual('konta osobiste', check_site_open_outerText,
                         f'Expected result after login: konta osobiste , differ from actual {check_site_open_outerText}')