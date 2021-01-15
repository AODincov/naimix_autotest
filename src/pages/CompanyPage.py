from src.pages.CompanyInfoPage import CompanyInfoPage
from src.pages.blocks.LeftNavigationBlock import LeftNavigationBlock
from selenium.webdriver.support import expected_conditions as ec
from src.core.WebElement import WebElement
from src.steps.AssertsSteps import AssertsSteps

# Поиск и создание компаний
from src.steps.BrowserSteps import BrowserSteps


class CompanyPage(LeftNavigationBlock):
    __dropdown_company_type_button: WebElement = WebElement(r"//i[@class='dropdown icon']")
    __cancel_button: WebElement = WebElement(r"//button[@class='ui basic button apply-buttons__cancel']")
    __create_company_button: WebElement = WebElement(r"//button")
    __info_about_customer_title: WebElement = WebElement(r"#root > div.layouts > div.layouts_content > div > "
                                                         "div.client-new__header > div")
    __close_content_button_with_load: WebElement = WebElement(r"//*[@id='root']/div[2]/div[3]/div/div/i")
    __close_content_button: WebElement = WebElement(r"///*[@id='root']/div[2]/div[3]/div/div/i")
    __load_content_icon: WebElement = WebElement(r"//*[@id='root']/div[2]/div[3]/div/div[@class='ui icon message']")
    __close_load_content: WebElement = WebElement(r"#root > div.layouts > div:nth-child(3) > div > div > i.close.icon")
    __business_registration_form_dropdown: WebElement = WebElement(r"//div[@name='clientType']//div[@class='menu "
                                                                   r"transition']//span")
    __category_dropdown: WebElement = WebElement(r"//div[@name='categoryId']//div[@class='menu "
                                                 r"transition']")
    __option_for_dropdown: WebElement = WebElement(r"//div[@role='option']")
    __add_button: WebElement = WebElement(r"//span[text()='Добавить']")

    __official_name_company_input: WebElement = WebElement(
        r"//input[@placeholder='Введите официальное название компании']")
    __short_name_company_input: WebElement = WebElement(
        r"//input[@placeholder='Введите сокращенное название компании']")
    __inn_input: WebElement = WebElement(r"//input[@placeholder='Введите ИНН']")
    __address_company_input: WebElement = WebElement(r"//input[@placeholder='Введите адрес компании']")
    __company_dropdown_button: WebElement = WebElement(
        r"//*[@id='root']/div[2]/div[2]/div/form/div[10]/div[2]/div[1]/i")
    __name_company_search_input: WebElement = WebElement(r"//input[@name='nameSubstringFilter']")
    __search_company_button: WebElement = WebElement(r"//span[text()='Найти']")

    @staticmethod
    def xpath_field_for_new_company(field):
        __xpath_field_new_company: WebElement = WebElement("//input[@placeholder='" + field + "']")
        return __xpath_field_new_company

    @staticmethod
    def xpath_for_company_in_search_table(short_name_company):
        __company_card_href: WebElement = WebElement(r"//a[text()='" + short_name_company + "']")
        return __company_card_href

    # todo переделать под возможность выбора элемента
    @staticmethod
    def xpath_for_select_category(select_field):
        __category_select: WebElement = WebElement(
            "//*[@id='root']/div[2]/div[2]/div/form/div[10]/div[2]/div[1]/div[2]/div[1]/span")
        #   r"//div[@name='categoryId']//div[@class='menu transition']/..//span[text()='" + select_field + "']/..")
        return __category_select

    @staticmethod
    def xpath_for_select_type(type_company):
        __type_company: WebElement = WebElement(
            "r//div[@class='visible menu transition']//div[@role='option']//span[text()='Иностранная организация']"
        )
        return __type_company

    @staticmethod
    def xpath_for_error_field_new_company(namefield, text_error):
        __field: WebElement = WebElement(
            r"//div[contains(text(),'" + namefield + "')]/..//div[text()='" + text_error + "']")
        return __field

    @staticmethod
    def close_content_list_task(driver):
        if AssertsSteps.check_exists_element(driver, CompanyPage.__load_content_icon.get()):
            driver.wait.until(
                ec.element_to_be_clickable(CompanyPage.__close_content_button_with_load.get())).click()
        else:
            driver.wait.until(ec.presence_of_element_located(CompanyPage.__close_content_button.get()))
            driver.wait.until(ec.element_to_be_clickable(CompanyPage.__close_content_button.get())).click()

    @staticmethod
    def click_create_company_button(driver):
        driver.wait.until(ec.presence_of_element_located(CompanyPage.__create_company_button.get())).click()
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.__info_about_customer_title.get()))

    @staticmethod
    def click_add_button_with_go_on_search_company(driver):
        driver.wait.until(ec.presence_of_element_located(CompanyPage.__add_button.get()))
        BrowserSteps.scroll_down(driver)
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.__add_button.get()))
        driver.wait.until(ec.element_to_be_clickable(CompanyPage.__add_button.get())).click()
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.__name_company_search_input.get()))

    @staticmethod
    def click_cancel_company_button(driver):
        driver.wait.until(ec.presence_of_element_located(CompanyPage.__cancel_button.get())).click()
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.__info_about_customer_title.get()))

    @staticmethod
    def assert_dropdown_business_registration_form(driver, list_for_check):
        AssertsSteps.assert_dropdown_div(driver, list_for_check,
                                         CompanyPage.__business_registration_form_dropdown.get())

    @staticmethod
    def assert_req_field(driver, *field):
        driver.wait.until(ec.presence_of_element_located(CompanyPage.__add_button.get())).click()
        for i in field:
            driver.wait.until(ec.visibility_of_element_located(
                CompanyPage.xpath_for_error_field_new_company(i, 'Обязательное поле').get()))
            print(i)


    @staticmethod
    def assert_error_inputs_field(driver, field, not_correct_values, error):
        for i in field:
            BrowserSteps.scroll_up(driver)
            driver.wait.until(ec.visibility_of_element_located(
                CompanyPage.xpath_field_for_new_company(not_correct_values))).send_keys(not_correct_values)
            # todo добавить проверку введенного значения
            BrowserSteps.scroll_down(driver)
            driver.wait.until(ec.presence_of_element_located(CompanyPage.__add_button.get())).click()
            BrowserSteps.scroll_up(driver)
            driver.wait.until(ec.visibility_of_element_located(
                CompanyPage.xpath_for_error_field_new_company(i, error).get()))

    @staticmethod
    def assert_not_req_field(driver, *field):
        driver.wait.until(ec.presence_of_element_located(CompanyPage.__add_button.get())).click()
        for i in field:
            AssertsSteps.check_not_exists_element(driver, CompanyPage.xpath_for_error_field_new_company(i,
                                                                                                        'Обязательное поле').get())

    @staticmethod
    def filed_req_field(driver, official_name_company, short_name_company, inn, address_company, category):
        driver.wait.until(
            ec.visibility_of_element_located(CompanyPage.__official_name_company_input.get())).send_keys(
            official_name_company)
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.__short_name_company_input.get())).send_keys(
            short_name_company)
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.__inn_input.get())).send_keys(inn)
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.__address_company_input.get())).send_keys(
            address_company)
        driver.wait.until(ec.element_to_be_clickable(CompanyPage.__company_dropdown_button.get())).click()
        driver.wait.until(
            ec.visibility_of_element_located(CompanyPage.xpath_for_select_category(category).get())).click()

    @staticmethod
    def search_company_with_go_on_info(driver, short_name_company):
        driver.wait.until(
            ec.visibility_of_element_located(CompanyPage.__name_company_search_input.get())).send_keys(
            short_name_company)
        driver.wait.until(ec.element_to_be_clickable(CompanyPage.__search_company_button.get())).click()
        driver.wait.until(
            ec.element_to_be_clickable(CompanyPage.xpath_for_company_in_search_table(short_name_company).get())).click()
        driver.wait.until(
            ec.visibility_of_element_located(CompanyInfoPage.xpath_title_info_page(short_name_company).get()))

    @staticmethod
    def select_type_client(driver):
        driver.wait.until(ec.element_to_be_clickable(CompanyPage.__company_dropdown_button.get()))
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.xpath_for_select_category("").get())).click()

    @staticmethod
    def select_type_company(driver, type_company):
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.__dropdown_company_type_button.get()))
        driver.wait.until(ec.element_to_be_clickable(CompanyPage.__dropdown_company_type_button.get())).click()
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.xpath_for_select_type(type_company).get()))
        driver.wait.until(ec.element_to_be_clickable(CompanyPage.xpath_for_select_type(type_company).get())).click()
