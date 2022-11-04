import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def get_chrome_options():
    options = Options()
    options.add_argument('chrome')  # Use headless
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    service = Service('C:/Program Files/Python310/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    return driver


@pytest.fixture(scope='function')
def setup(get_webdriver, request):
    driver = get_webdriver
    url = 'https://www.youtube.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
