from src.initalization.BaseTest import BaseTest
from src.pages.CompanyPage import CompanyPage
from src.steps.BaseSteps import BaseSteps

# АдминНаймикса/Компании/Добавить компанию Иностранную организацию - кнопка "отменить"
class Test_Namemix_T1914(BaseTest):
    __short_name_company = "Тестовое сокращенное название компании " + BaseSteps.den_random_str(3)

    def test_namemix_t1914(self, resource):
        BaseTest.login(self, login="nmadmin", password="nmadmin123")
        CompanyPage.close_content_list_task(self.driver)
        CompanyPage.click_create_company_button(self.driver)
        CompanyPage.select_type_company(self.driver, "Иностранная организация")
        CompanyPage.assert_dropdown_business_registration_form(self.driver, ["Юридическое лицо",
                                                                                 "Индивидуальный предприниматель",
                                                                                 "Иностранная организация"])
        CompanyPage.assert_req_field(self.driver, "Официальное название компании", "Сокращенное название компании",
                                         "ИНН", "Фактический адрес", "Категория")
        CompanyPage.filed_req_field(self.driver,
                                        "Тестовое название компании " + BaseSteps.den_random_str(5),
                                        Test_Namemix_T1914.__short_name_company,
                                        "3778591896",
                                        "Тестовый адресс компании" + BaseSteps.den_random_str(5), "Аренда")
        CompanyPage.click_cancel_company_button(self.driver)
        CompanyPage.search_company_with_go_on_info(self.driver, Test_Namemix_T1914.__short_name_company)