from selenium.webdriver.chrome.webdriver import WebDriver

from src.initalization.Initialize import Initialize


class BaseTest:
    driver = Initialize.get_driver()

