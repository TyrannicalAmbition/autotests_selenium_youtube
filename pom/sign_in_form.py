from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class SignInForm(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.sign_in_button: str = '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div'
        self.login_omnibox: str = '//*[@id="identifierId"]'
        self.next_button: str = '//*[@id="identifierNext"]/div/button'

    def get_sign_in_button(self) -> WebElement:
        return self.is_visible('xpath', self.sign_in_button, 'Sign in')

    def get_login_omnibox(self) -> WebElement:
        return self.is_visible('xpath', self.login_omnibox, 'Login omnibox')

    def get_next_button(self):
        return self.is_visible('xpath', self.next_button, 'Next button')
