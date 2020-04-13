from selenium.common.exceptions import NoSuchElementException
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_presented(self, css_selector, id):
        try:
            self.browser.find_element(css_selector, '#id')
        except(NoSuchElementException):
            return False
        return True

