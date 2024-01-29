import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getuserpassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        # self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        time.sleep(10)
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(5)


        self.logger.info("************* searching customer by Name **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(10)
        status = searchcust.searchCustomerByName("Victoria Terces")
        print("Status:", status)
        self.driver.close()

        assert True == status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")
