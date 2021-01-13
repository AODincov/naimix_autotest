import random
from string import ascii_uppercase

from selenium.webdriver.support.select import Select


class BaseSteps:

    @staticmethod
    def den_random_int(len_int):
        a = random.randint(0, 9)
        i = ''
        while len_int == 0:
            i += str(a)
            len_int -= 1
        return i

    @staticmethod
    def den_random_str(len_str):
        i = ''.join(random.choice(ascii_uppercase) for i in range(len_str))
        return i

    @staticmethod
    def select_from_dropdown(driver, dropdown_path, field):
        dropdown = Select(driver.find_element(dropdown_path))
        dropdown.select_by_visible_text(field)
