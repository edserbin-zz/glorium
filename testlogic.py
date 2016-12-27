from basetest import BaseTest
from pages.advertpage import AdvertPage
from pages.authpage import AuthPage
from pages.mainpage import MainPage


class TestLogic(BaseTest):

    def close_noisy_window(self):
        self.page.close_sms_verification()

    def registrate_new_user(self, user_info):
        self.page = AuthPage(self.driver)
        self.page.registrate_new_user(user_info)

    def login(self, user_info):
        self.page = AuthPage(self.driver)
        self.page.login(user_info)

    def make_advertisement(self, advertisement_info):
        self.close_noisy_window()
        self.page = AdvertPage(self.driver)
        self.page.place_advertisement(advertisement_info)
        self.assertTrue(self.page.is_message_show())

    def make_advertisement_for_new_user(self, advertisement_info, user_info, mail):
        self.page = MainPage(self.driver)
        self.page.make_advertisement()
        if "account" in self.driver.current_url:
            self.registrate_new_user(user_info)
            # get link from email and activate account
            self.driver.get(mail.get_link_from_email_by_number(1))
        self.page.make_advertisement()
        self.make_advertisement(advertisement_info)

    def make_advertisement_for_existing_user(self, advertisement_info, user_info):
        self.page = MainPage(self.driver)
        self.page.make_advertisement()
        if "account" in self.driver.current_url:
            self.login(user_info)
        self.make_advertisement(advertisement_info)
