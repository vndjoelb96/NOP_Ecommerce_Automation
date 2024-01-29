import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getapplicationURL()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getuserpassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepagetitle(self, setup):
        self.logger.info("************* Test_001_Login ************")
        self.logger.info("************* Verifying Homepage title ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************* Verifying Homepage title is PASSED ************")
        else:
            self.driver.save_screenshot(
                "/Users/vinodjoel/PycharmProjects/nopcommerce_app/Screenshots/test_homepagetitle.png")
            self.driver.close()
            self.logger.error("************* Verifying Homepage title is FAILED ************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************* Login test is started ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************* Login test title is PASSED ************")
            self.driver.close()
        else:
            self.driver.save_screenshot("/Users/vinodjoel/PycharmProjects/nopcommerce_app/Screenshots/test_login.png")
            self.driver.close()
            self.logger.error("************* Login test title is FAILED ************")
            assert False
