from src.pages.blocks.LeftNavigationBlock import LeftNavigationBlock
from selenium.webdriver.support import expected_conditions as ec

from src.core.WebElement import WebElement


class CompanyInfoPage(LeftNavigationBlock):
    __client_contact_info: WebElement = WebElement("div.client-contact-info.container-fluid")

    @staticmethod
    def is_open(driver):
        driver.wait.until(ec.visibility_of_element_located(CompanyInfoPage.__client_contact_info.get()))
