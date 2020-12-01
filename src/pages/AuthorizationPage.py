from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class AuthorizationPage:
    __login_button = (By.XPATH, "//button")
    __email_input = (By.XPATH, "//input[@placeholder='E-mail']")
    __password_input = (By.XPATH, "//input[@placeholder='Пароль']")

    @staticmethod
    def login(driver, login: str, password:str):
        driver.wait.until(ec.element_to_be_clickable(AuthorizationPage.__email_input.get())).send_keys(login)
        driver.wait.until(ec.element_to_be_clickable(AuthorizationPage.__password_input.get())).send_keys(password)
        driver.wait.until(ec.element_to_be_clickable(AuthorizationPage.__login_button.get())).click()

    @staticmethod
    def is_open(driver):
        driver.wait.until(ec.visibility_of_element_located(AuthorizationPage.__login_button.get()))
