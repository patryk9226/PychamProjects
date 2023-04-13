from selenium.webdriver.common.by import By

def user_login(driver, user_email, user_pass):
    """Login user to e-shop lost hat using given email and password

    :param driver: webdriver instance
    :param user_email: email to login user
    :param user_pass: password to login user
    :return: None
    """
    # wpisnaie loginu
    email_input_element = driver.find_element(By.XPATH, "//*[@class='form-control']")
    email_input_element.send_keys(user_email)
    # wpisanie hasła
    password_input_element = driver.find_element(By.XPATH,
                                                 "//*[@class='form-control js-child-focus js-visible-password']")
    password_input_element.send_keys(user_pass)
    # kliknięcie w zaloguj
    sign_in_button_element = driver.find_element(By.XPATH, "//*[@class='btn btn-primary']")
    sign_in_button_element.click()