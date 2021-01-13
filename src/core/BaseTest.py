import pytest

from src.initalization.Initialize import Initialize


class BaseTest:
    driver = Initialize.get_driver()
    print(driver.session_id)

    @pytest.fixture
    def base_test(self):
        yield
        self.driver.close()
        self.driver.quit()
