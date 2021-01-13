import pytest

from src.initalization.Initialize import Initialize


class BaseTest:
    driver = Initialize.get_driver()

    @pytest.fixture
    def base_test(self):
        yield
        self.driver.close()

