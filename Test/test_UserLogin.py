import time

import pytest
from selenium.webdriver.common.by import By

from PageObject.UserLogin import LoginWithCredentials
from Utilities.BaseClass import BaseClass


class TestUserLogin(BaseClass):

    # marking up as a mark up for regression test suite
    @pytest.mark.regression
    def test_UserLogin(self):
        # clicking blink text on login page
        LoginWithCredentials.clickBlinkText(self)

        # managing window tabs
        self.managebrowsertab(1)

        # storing string into variable
        mailText = self.driver.find_element(By.XPATH, "//a[@href='mailto:mentor@rahulshettyacademy.com']").text

        # printing text
        print(mailText)

        # returning to main window
        self.managebrowsertab(0)

        # entering the credentials in login page
        LoginWithCredentials.login(self, "test@test.com", "12345")

        # grabing error text into variable
        errorText = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger col-md-12']/strong").text
        print(errorText)

        # LoginWithCredentials.login(self, "contentadmin", "Ctadmin@1234")
        # self.getLogger().info("User is logged in sucessfully")

    # marking up as a mark up for smoke test suite
    @pytest.mark.smoke
    def test_UserLoginUsing_Constructor(self):
        login_Process = LoginWithCredentials(self.driver)
        login_Process.login("contentadmin", "Ctadmin@12345")
        self.verifyelementpresent("//h2[text()='Content in review']")
        # //h2[text()='Content in review']
        actualurl = self.driver.current_url
        assert "https://cms-dev.monotype.com/user/8661/moderation/dashboard?check_logged_in=1" == actualurl
