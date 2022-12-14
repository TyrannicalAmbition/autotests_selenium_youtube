from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#items>ytd-guide-entry-renderer'
        self.sign_in_button: str = '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div'
        self.__search_bar: str = '//*[@id="search-input"]/div'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_sign_in_button(self) -> WebElement:
        return self.is_visible('xpath', self.sign_in_button, 'Sign in')
