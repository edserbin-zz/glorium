import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    url = 'https://www.olx.ua'
    new_advertisement_xpath = '//*[@id="postNewAdLink"]'
    sms_verification_close_xpath = '//*[@id="smsVerificationContainer"]//*[@id="fancybox-close"]'
    sms_box_xpath = '//*[@id="fancybox-outer"]'

    def __init__(self, driver):
        self.driver = driver
        self.waiting_time = 20

    def navigate(self):
        self.driver.get(self.url)

    def enter_text_into_field(self, xpath, text):
        """
        my wrapper for entering keys
        """
        self.wait_until_object_appears(xpath)
        field = self.driver.find_element_by_xpath(xpath)
        field.send_keys(text)

    def click_on_the_object(self, xpath):
        """
        my wrapper for entering keys
        """
        self.wait_until_object_appears(xpath)
        elem = self.driver.find_element_by_xpath(xpath)
        elem.click()

    def wait_until_object_appears(self, xpath):
        """
        this function wait until object appears, becomes visible
        and clickable
        """
        try:
            WebDriverWait(self.driver, self.waiting_time).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print('Element is not exist on page, xpath ' + xpath)
        try:
            WebDriverWait(self.driver, self.waiting_time).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print('Element is not visible on page, xpath ' + xpath)
        try:
            WebDriverWait(self.driver, self.waiting_time).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            print('Element is not clickable on page, xpath ' + xpath)

    def make_advertisement(self):
        self.click_on_the_object(self.new_advertisement_xpath)

    def close_sms_verification(self):
        old_time = self.waiting_time
        self.driver.switch_to_active_element()
        self.waiting_time = 3
        try:
            self.click_on_the_object(self.sms_verification_close_xpath)
            self.click_on_the_object("//*[contains(text(), '%s')]" % 'Отменить подтверждение')
        except:
            pass
        finally:
            self.waiting_time = old_time
        time.sleep(2)

    def close_cookie_messange(self):
        self.click_on_the_object('//*[@class="cookiesBarClose abs close"]')

    def is_message_show(self):
        try:
            self.wait_until_object_appears(self.sms_box_xpath)
            # self.driver.find_element_by_xpath(self.sms_box_xpath)
        except NoSuchElementException:
            return False
        return True
