import os
import unittest

from datetime import datetime

from selenium import webdriver

import browsersettings
from pages.mainpage import MainPage


def check_failed(f):
    """
    function wrapper for making reports
    """
    def wrapper(*args):
        try:
            return f(*args)
        except Exception as e:
            print(e)
            args[0].make_report()
            raise e
    return wrapper


class BaseTest(unittest.TestCase):

    def setUp(self):
        """
        this function defines the start settings
        """
        self.select_driver(browsersettings.browser)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(MainPage.url)

    def make_report(self):
        """
        function which describes behavior when the test is failed
        """
        print('-----------------------------------------')
        print("FAILED LINK:  " + self.driver.current_url)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.driver.get_screenshot_as_file('screenshot-%s.png' % now)
        print('-----------------------------------------')

    def tearDown(self):
        """
        this function defines the actions after test is over
        """
        self.driver.quit()

    def select_driver(self, driver='chrome'):
        """
        this function need for select a browser
        """
        pathname = os.path.dirname(__file__)
        if driver == 'chrome':
            self.driver = webdriver.Chrome(executable_path=pathname + '/drivers/chromedriver')
        if driver == 'firefox':
            self.driver = webdriver.Firefox(executable_path=pathname + '/drivers/geckodriver')
