import unittest

from base.driver_init import driver_init
from pages.header import Header
from pages.login_page import LoginPage
from utils import get_all_


class TestHeader(unittest.TestCase):
    def setUp(self):
        self.driver = driver_init()
        data = get_all_("ADMIN_USER")
        lp = LoginPage(self.driver).load()
        lp.login(data["username"], data["password"])
        lp.wait_until_dashboard_load()


    def tearDown(self):
        self.driver.quit()

    def test_signout(self):
        self.header = Header(self.driver)
        self.header.logout()
        self.assertTrue(LoginPage(self.driver).get_title(), "LOGIN Panel")


if __name__ == '__main__':
    unittest.main()
