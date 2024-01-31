import inspect
import logging
import time

# from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass():

    # Logger is used to print logs in html reports or in report portal
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        logger.debug("A debug logger is executed")
        logger.info("A info logger is executed")
        logger.warning("A warning logger is executed")
        logger.error("A error logger is executed")
        logger.critical("A critical logger is executed")
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.CRITICAL)
        return logger

    # verifying xpath element using explicit wait
    def verifyelementpresent(self, xpath):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))

    # handling windows tab using window_handles method via selenium
    def managebrowsertab(self, index):
        windowsOpened = self.driver.window_handles
        self.driver.switch_to.window(windowsOpened[index])
        time.sleep(2)
