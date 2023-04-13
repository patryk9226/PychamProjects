from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service('C:\TestFiles\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
title = driver.title
print(title)
assert 'Demobank - Bankowość Internetowa - Logowanie' == title
time.sleep(2)