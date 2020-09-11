from utils.base_class import BaseClass
import pytest
from page_objects.login_page import LoginPage


class TestLogin(BaseClass):

    @pytest.mark.amazon
    def test_1(self):
        login_page = LoginPage(self.driver)
        print("Test login to amazon")
        self.driver.get("https://www.amazon.in/")
        login_page.get_search_bar().send_keys("M51")
        login_page.get_search_button().click()
        import time
        time.sleep(5)

    def test_2(self):
        print("Test search in amazon")
