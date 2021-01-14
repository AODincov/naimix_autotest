from src.initalization.BaseTest import BaseTest


class Test_authorization(BaseTest):

    def test_authorization(self):
        BaseTest.login(self, login="admin@admin.ru", password="Aa123456")
        BaseTest.close(self)
