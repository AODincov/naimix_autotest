from selenium import webdriver
from resources.configuration import CHROME_PATH
from selenium.webdriver.support.ui import WebDriverWait


class Initialize:

    @staticmethod
    def get_driver():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(CHROME_PATH, chrome_options=chrome_options)
        driver.wait = WebDriverWait(driver, 60)

        return driver
