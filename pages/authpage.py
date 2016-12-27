from pages.basepage import BasePage


class AuthPage(BasePage):

    url = BasePage.url + '/account/'
    register_tab_xpath = '//*[@id="register_tab"]'
    login_tab_xpath = '//*[@id="login_tab"]'
    email_xpath = '//*[@id="userEmailRegister"]'
    login_xpath = '//*[@id="userEmail"]'
    password_xpath = '//*[@id="userPassRegister"]'
    user_password_xpath = '//*[@id="userPass"]'

    accept_terms_xpath_on_register_form = '//*[@id="registerForm"]//label[2]'
    register_button_xpath = '//*[@id="register"]'
    login_button_xpath = '//*[@id="se_userLogin"]'

    def registrate_new_user(self, user_info):
        self.select_register_tab()
        self.enter_email(user_info.get('email'))
        self.enter_password(user_info.get('password'))
        self.accept_terms()
        self.click_register()

    def login(self, user_info):
        self.select_login_tab()
        self.enter_login(user_info.get('email'))
        self.enter_user_password(user_info.get('password'))
        self.click_login()

    def select_register_tab(self):
        self.click_on_the_object(self.register_tab_xpath)

    def enter_email(self, email):
        self.enter_text_into_field(self.email_xpath, email)

    def enter_password(self, password):
        self.enter_text_into_field(self.password_xpath, password)

    def accept_terms(self):
        self.click_on_the_object(self.accept_terms_xpath_on_register_form)

    def click_register(self):
        self.click_on_the_object(self.register_button_xpath)

    def select_login_tab(self):
        self.click_on_the_object(self.login_tab_xpath)

    def enter_login(self, login):
        self.enter_text_into_field(self.login_xpath, login)

    def enter_user_password(self, password):
        self.enter_text_into_field(self.user_password_xpath, password)

    def click_login(self):
        self.click_on_the_object(self.login_button_xpath)




