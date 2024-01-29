import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils


# Here we are trying to test the login credentials from
# Excel sheet in the website https://admin-demo.nopcommerce.com/

class Test_002_DDT_Login:
    baseUrl = ReadConfig.getapplicationURL()
    path = "TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************* Test_002_DDT_Login started ************")
        self.logger.info("************* Verify Login DDT test ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("No of rows in excel", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.status = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            # Check for Matching title, if title matched/unmatched check for PASS FAIL in status column in excel sheet
            if act_title == exp_title:
                if self.status == "Pass":
                    self.logger.info('***Test is passed***')
                    self.lp.clickLogout()
                    lst_status.append('PASS')
                elif self.status == "Fail":
                    self.logger.info('***Test is Failed***')
                    self.lp.clickLogout()
                    lst_status.append('FAIL')
            elif act_title != exp_title:  # login status is passed but title mismatch then test fail
                if self.status == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.status == 'Fail':  # login status is fail and title mismatch then test pass
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)

            # After appending all status to list if we have all PASS status then test is Pass else Fail
        if "Fail" not in lst_status:
                self.logger.info("******* DDT Login test passed **********")
                self.driver.close()
                assert True
        else:
                self.logger.error("******* DDT Login test failed **********")
                self.driver.close()
                assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  Test_002_DDT_Login ************* ");
