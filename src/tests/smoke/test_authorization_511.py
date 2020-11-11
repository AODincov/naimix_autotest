from src.initalization.Initialize import Initialize

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from src.pages.AuthorizationPage import AuthorizationPage
from src.pages.LandingPage import LandingPage

from src.blocks.LeftNavigationBlock import LeftNavigationBlock


class TestAuthorization(Initialize):
    def test_authorization(self):
        driver = self.get_driver()
        driver.get('https://nm-test.mmtr.ru/')
        wait = WebDriverWait(driver, 60)
        wait.until(ec.element_to_be_clickable([By.CSS_SELECTOR,
                                               LandingPage.login_button]))
        driver.find_element_by_css_selector(LandingPage.login_button).click()

        wait.until(ec.element_to_be_clickable([By.XPATH, AuthorizationPage.login_button]))
        driver.find_element_by_xpath(AuthorizationPage.email_input).send_keys("admin@admin.ru")
        driver.find_element_by_xpath(AuthorizationPage.password_input).send_keys("Aa123456")
        driver.find_element_by_xpath(AuthorizationPage.login_button).click()

        wait.until(ec.visibility_of_element_located([By.XPATH, LeftNavigationBlock.block_base_path]))
