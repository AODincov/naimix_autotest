import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CHROME_PATH_FOR_WINDOWS = os.path.join(BASE_DIR, "resources", "chromedriver.exe")
CHROME_PATH_FOR_LINUX = os.path.join(BASE_DIR, "resources", "chromedriver")
TIMEOUT = 60
