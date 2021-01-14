from selenium.webdriver.support.wait import WebDriverWait
from resources.configuration import CHROME_PATH
from selenium import webdriver
import requests
from requests.adapters import HTTPAdapter
import urllib3
from urllib3.util.retry import Retry
import time
from selenium.webdriver.support import expected_conditions as ec

from src.core.WebElement import WebElement


class BaseTest(object):
    url = 'https://nm-test.mmtr.ru/'
    config = 'chrome'

    def get_driver(self):
        if self.config == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("disable-infobars")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            self.driver = webdriver.Chrome(CHROME_PATH, chrome_options=chrome_options)
            self.driver.implicitly_wait(15)
            print("Running tests on Chrome driver")
        elif self.config == 'ie':
            self.driver = webdriver.Ie()
            print("Running tests on Internet Explorer driver")
            self.driver.implicitly_wait(15)
        elif self.config == 'firefox':
            self.driver = webdriver.Firefox()
            print("Running tests on Firefox driver")
            self.driver.implicitly_wait(15)
        elif self.config == 'None':
            print('No driver type specified....')

    def login(self, login, password):
        try:
            self.get_driver()
            self.driver.get(self.url)
            self.driver.wait = WebDriverWait(self.driver, 60)
            self.driver.wait.until(ec.element_to_be_clickable(WebElement("//input[@placeholder='E-mail']").get()))
            self.driver.wait.until(
                ec.element_to_be_clickable(WebElement("#root > div.login__wrapper > div.login-cookie > div > "
                                                      "div.login-cookie__button").get())).click()
            self.driver.wait.until(ec.visibility_of_element_located(WebElement("//button").get()))
            self.driver.wait.until(
                ec.element_to_be_clickable(WebElement("//input[@placeholder='E-mail']").get())).send_keys(login)
            self.driver.wait.until(
                ec.element_to_be_clickable(WebElement("//input[@placeholder='Пароль']").get())).send_keys(
                password)
            self.driver.wait.until(ec.element_to_be_clickable(WebElement("//button").get())).click()
            self.driver.wait.until(
                ec.visibility_of_element_located(WebElement("//div[contains(@class ,'nmx-menu')]").get()))
            time.sleep(5)
        except requests.ConnectionError as e:
            print("******Connection error encountered! Trying again....")
            print(str(e))
            time.sleep(10)
        except requests.Timeout as e:
            print("*****Timeout Error!********")
            print(str(e))
        except requests.RequestException as e:
            time.sleep(30)
            print("*******Server rejected the requests, too many requests!*******")
            print(str(e))
        except KeyboardInterrupt:
            print("*********User interruption detected*******")
        except ConnectionRefusedError as e:
            time.sleep(30)
            print(str(e))
            print("*********Portal Connection refused by the server**********")

        except urllib3.exceptions.NewConnectionError as e:
            print(str(e))
            print("********Portal New connection timed out***********")
            time.sleep(30)

        except urllib3.exceptions.MaxRetryError as e:
            print(str(e))
            time.sleep(30)
            print("*********Portal Max tries exceeded************")
        except urllib3.exceptions.ConnectTimeoutError as e:
            time.sleep(10)
            print("**********Timeout error************")
        except urllib3.exceptions.ClosedPoolError as e:
            time.sleep(10)
            print(str(e))
        except urllib3.exceptions.HTTPError as e:
            time.sleep(10)
            print(str(e))
        self.driver.implicitly_wait(3)

    # Closing the driver window and terminating the test
    def close(self):
        self.driver.close()

    def tearDown(self):
        self.driver.close()
    # if __name__ == '__main__':
    #  Driver().login()
    #  Driver().close()
