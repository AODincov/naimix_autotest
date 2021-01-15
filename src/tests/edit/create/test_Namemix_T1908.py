from src.initalization.BaseTest import BaseTest
from src.pages.CompanyPage import CompanyPage

# todo добавить проверки значений полей + проверки чекбоксов
# АдминНаймикса/Компании/Добавить компанию ИП - валидация
class Test_Namemix_T1908(BaseTest):

    def test_namemix_t1908(self, resource):
        BaseTest.login(self, login="nmadmin", password="nmadmin123")
        CompanyPage.close_content_list_task(self.driver)
        CompanyPage.click_create_company_button(self.driver)
        CompanyPage.select_type_company(self.driver, "Индивидуальный предприниматель")
        CompanyPage.assert_dropdown_business_registration_form(self.driver, ["Юридическое лицо",
                                                                                 "Индивидуальный предприниматель",
                                                                                 "Иностранная организация"])
        assert_req_field(self.driver, "Официальное название компании", "Сокращенное название компании",
                                         "ИНН", "Фактический адрес", "Категория")
        CompanyPage.assert_not_req_field(self.driver, "ФИО контактного лица", "Телефон контактного лица", "ИНН",
                                             "E-mail контактного лица", "Промо-код")