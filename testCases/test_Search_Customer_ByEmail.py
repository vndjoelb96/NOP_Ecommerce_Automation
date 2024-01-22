import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getuserpassword()
    logger = LogGen.loggen()  # Logger


    def test_searchCustomerByEmail(self,setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        time.sleep(5)
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(5)

        self.logger.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        time.sleep(5)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        print(searchcust)
        time.sleep(5)
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        print(status)
        time.sleep(5)
        assert True==status
        self.driver.close()
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")