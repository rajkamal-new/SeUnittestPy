import unittest

from ddt import ddt, data, unpack

from base.driver_init import driver_init
from pages.login_page import LoginPage
from utils import get_all_
from utils.csv_reader import get_csv_data


@ddt
class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = driver_init()

    def tearDown(self):
        self.driver.quit()


    def test_1_login_success(self):
        data = get_all_("ADMIN_USER")
        lp = LoginPage(self.driver).load()
        lp.login(data["username"], data["password"])
        self.assertTrue(lp.wait_until_dashboard_load())


    @data(*get_csv_data("/../data/t1/invalid_login_data.csv"))
    @unpack
    def test_2_login_fail(self, username, password, err_msg):
        lp = LoginPage(self.driver).load()
        lp.login(username, password)
        self.assertEqual(lp.get_err_msg(), err_msg)


if __name__ == "__main__":
    unittest.main()