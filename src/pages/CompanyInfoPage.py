from src.pages.blocks.LeftNavigationBlock import LeftNavigationBlock
from selenium.webdriver.support import expected_conditions as ec
from src.core.WebElement import WebElement
from src.steps.AssertsSteps import AssertsSteps


class CompanyInfoPage(LeftNavigationBlock):
    __create_company_button: WebElement = WebElement(r"//button")
    __title_info_about_customer: WebElement = WebElement(r"#root > div.layouts > div.layouts_content > div > "
                                                         "div.client-new__header > div")
    __close_content: WebElement = WebElement(r"//*[@id='root']/div[2]/div[3]/div/div/i")
    __load_content: WebElement = WebElement(r"//*[@id='root']/div[2]/div[3]/div/div[@class='ui icon message']")
    __close_load_content: WebElement = WebElement(r"#root > div.layouts > div:nth-child(3) > div > div > i.close.icon")
    __business_registration_form_dropdown: WebElement = WebElement(r"//div[@name='clientType']//div[@class='menu "
                                                                   r"transition']//span")
    __option_for_dropdown: WebElement = WebElement(r"//div[@role='option']")

    @staticmethod
    def is_open(driver):
        driver.wait.until(ec.element_to_be_clickable(CompanyInfoPage.__create_company_button.get()))

    @staticmethod
    def close_content_list_task(driver):
        if AssertsSteps.check_exists_by_xpath(driver, CompanyInfoPage.__load_content.get()):
            driver.wait.until(ec.element_to_be_clickable(CompanyInfoPage.__close_load_content.get())).click()
        else:
            driver.wait.until(ec.presence_of_element_located(CompanyInfoPage.__close_content.get()))
            driver.wait.until(ec.element_to_be_clickable(CompanyInfoPage.__close_content.get())).click()

    @staticmethod
    def click_create_company_button(driver):
        driver.wait.until(ec.presence_of_element_located(CompanyInfoPage.__create_company_button.get())).click()
        driver.wait.until(ec.visibility_of_element_located(CompanyInfoPage.__title_info_about_customer.get()))

    @staticmethod
    def assert_dropdown_business_registration_form(driver, list_for_check):
        AssertsSteps.assert_dropdown_div(driver, list_for_check,
                                         CompanyInfoPage.__business_registration_form_dropdown.get())
