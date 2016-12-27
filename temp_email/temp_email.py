import time
from tempmail import TempMail
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.result = []

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
            # Check the list of defined attributes.
            for name, value in attrs:
                # If href is defined, print it.
                if name == "href":
                    self.result.append(value)


# https://pypi.python.org/pypi/temp-mail
class TempEmail(object):
    def __init__(self):
        self.tm = TempMail()
        self.email = self.tm.get_email_address()

    # this method will wait the needed for us email
    # if you send number_of_email=3 , this method will
    # wait a third email and return link from it
    def get_link_from_email_by_number(self, number_of_email, number_of_link=1):
        delay = 5
        start_time = time.time()
        while True:
            time.sleep(delay)
            mail = self.tm.get_mailbox(self.email)
            current_time = time.time()
            end_time = current_time - start_time
            # if the letter doesnt come in 10 minutes function will return None
            if end_time > 600:
                print('Message hasn`t came more than 10 minutes')
                return None
            if isinstance(mail, list) and len(mail) == number_of_email:
                mail = self.tm.get_mailbox(self.email)[number_of_email - 1]
                html = mail.get('mail_text_only')
                parser = MyHTMLParser()
                parser.feed(html)
                return parser.result[number_of_link]


