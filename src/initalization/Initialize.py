import platform
from selenium import webdriver
from resources.configuration import CHROME_PATH_FOR_LINUX
from resources.configuration import CHROME_PATH_FOR_WINDOWS
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

        if platform.system() == "Windows":
            new_drier = webdriver.Chrome(CHROME_PATH_FOR_WINDOWS, chrome_options=chrome_options)
            new_drier.wait = WebDriverWait(new_drier, 60)
        elif platform.system() == "linux":
            new_drier = webdriver.Chrome(CHROME_PATH_FOR_LINUX, chrome_options=chrome_options)
            new_drier.wait = WebDriverWait(new_drier, 60)

        return new_drier
