import unittest

from basetest import check_failed
from temp_email.temp_email import TempEmail
from testlogic import TestLogic


class TaskOne(TestLogic):

    @check_failed
    def test_make_advertisement_for_existing_user(self):
        user_info = {'email': 'edserbintest1@gmail.com',
                     'password': 'password1006'}
        advertisement_info = {'title': 'Test title',
                              'target': ['7', 'Строительство / ремонт / уборка', 'Cтроительные услуги'],
                              'type': '0',
                              'description': 'Test description and some more text',
                              'contact': {'address': 'Kiev',
                                          'name': 'Ed'}}
        self.make_advertisement_for_existing_user(advertisement_info, user_info)
        self.driver.get_screenshot_as_file('success of test 1.png')

    @check_failed
    def test_make_advertisement_for_new_user(self):
        mail = TempEmail()
        user_info = {'email': mail.email,
                     'password': 'password1006'}
        advertisement_info = {'title': 'Test title',
                              'target': ['7', 'Строительство / ремонт / уборка', 'Cтроительные услуги'],
                              'type': '0',
                              'description': 'Test description',
                              'contact': {'address': 'Kiev',
                                          'name': 'Ed'}}
        self.make_advertisement_for_new_user(advertisement_info, user_info, mail)
        self.driver.get_screenshot_as_file('success of test 2.png')

if __name__ == '__main__':
    unittest.main()
