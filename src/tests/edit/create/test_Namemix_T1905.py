from src.core.BaseTest import BaseTest
from src.pages.AuthorizationPage import AuthorizationPage
from src.pages.CompanyPage import CompanyPage


# todo добавить проверки значений полей + проверки чекбоксов
class Test_Namemix_T1905(BaseTest):

    def test_namemix_t1905(self, base_test):
        AuthorizationPage.full_login(self.driver, "nmadmin", "nmadmin123")
        CompanyPage.close_content_list_task(self.driver)
        CompanyPage.click_create_company_button(self.driver)
        CompanyPage.assert_dropdown_business_registration_form(self.driver, ["Юридическое лицо",
                                                                                 "Индивидуальный предприниматель",
                                                                                 "Иностранная организация"])
        CompanyPage.assert_req_field(self.driver, "Официальное название компании", "Сокращенное название компании",
                                         "ИНН", "Фактический адрес", "Категория")
        CompanyPage.assert_not_req_field(self.driver, "ФИО контактного лица", "Телефон контактного лица", "ИНН",
                                             "E-mail контактного лица", "Промо-код")
