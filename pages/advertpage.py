from selenium.webdriver.support.select import Select

from pages.basepage import BasePage


class AdvertPage(BasePage):

    title_xpath = '//*[@id="add-title"]'
    target_xpath = '//*[@id="choose-category-ilu"]'
    description_xpath = '//*[@id="add-description"]'
    city_xpath = '//*[@id="mapAddress"]'
    person_xpath = '//*[@id="add-person"]'
    private_business_xpath = '//*[@id="targetid_private_business"]'
    select_private_business_xpath = '//*[@id="id_private_business"]'
    save_xpath = '//*[@class="button big4 br3 large"]'

    def place_advertisement(self, advertisement_info):
        self.enter_title(advertisement_info.get('title'))
        self.select_target(advertisement_info.get('target'))
        self.choose_type(advertisement_info.get('type'))
        self.enter_description(advertisement_info.get('description'))
        self.enter_contact(advertisement_info.get('contact'))
        self.close_cookie_messange()
        self.save_advertisement()

    def enter_title(self, title):
        self.enter_text_into_field(self.title_xpath, title)

    def select_target(self, target):
        self.click_on_the_object(self.target_xpath)
        self.driver.switch_to_active_element()
        self.click_on_the_object('//*[@id="cat-%s"]' % target[0])
        self.click_on_the_object("//*[contains(text(), '%s')]" % target[1])
        self.click_on_the_object("//*[contains(text(), '%s')]" % target[2])

    def choose_type(self, type_of):
        self.close_sms_verification()
        self.click_on_the_object(self.private_business_xpath)
        self.click_on_the_object('//*[@id="targetid_private_business"]/dd/ul/li[%s]/a' % str(2+int(type_of)))

    def enter_description(self, description):
        self.enter_text_into_field(self.description_xpath, description)

    def enter_contact(self, contact):
        self.enter_addres(contact.get('address'))
        self.enter_name(contact.get('name'))

    def enter_addres(self, address):
        self.enter_text_into_field(self.city_xpath, address)

    def enter_name(self, name):
        self.enter_text_into_field(self.person_xpath, name)

    def save_advertisement(self):
        self.click_on_the_object(self.save_xpath)
