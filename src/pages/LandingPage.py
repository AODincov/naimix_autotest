from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class LandingPage:
    __login_button = (By.CSS_SELECTOR, "#root > div.home > header > div > div > a > div")

    @staticmethod
    def open_login_page(driver):
        driver.wait.until(ec.element_to_be_clickable(LandingPage.__login_button)).click()

        #todo Местами встречал такой возврат в примерах, но чет хз
        #return AuthorizationPage

    @staticmethod
    def is_open(driver):
        driver.wait.until(ec.visibility_of_element_located(LandingPage.__login_button))
