from src.core.BaseTest import BaseTest
from src.pages.AuthorizationPage import AuthorizationPage
from src.pages.CompanyInfoPage import CompanyInfoPage


class Test_Namemix_T1905(BaseTest):

    def test_namemix_t1905(self, base_test):
        AuthorizationPage.full_login(self.driver, "nmadmin", "nmadmin123")
        CompanyInfoPage.close_content_list_task(self.driver)
        CompanyInfoPage.click_create_company_button(self.driver)
        CompanyInfoPage.assert_dropdown_business_registration_form(self.driver, ["Юридическое лицо", "Индивидуальный предприниматель", "Иностранная организация"])
