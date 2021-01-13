from src.core.BaseTest import BaseTest
from src.pages.AuthorizationPage import AuthorizationPage

class TestAuthorization(BaseTest):

    def test_authorization(self, base_test):
        AuthorizationPage.open_login_page(self.driver)
        AuthorizationPage.close_cookie_login(self.driver)
        AuthorizationPage.is_open(self.driver)
        AuthorizationPage.login(self.driver, login="admin@admin.ru", password="Aa123456")
