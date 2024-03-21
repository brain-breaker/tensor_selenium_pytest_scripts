from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from pytest import fixture
from os import getcwd


@fixture
def browser():
    service = ChromeService(ChromeDriverManager().install())
    options = ChromeOptions()
    preferences = {'download.default_directory': getcwd(),
                   'safebrowsing.enabled': 'false'}
    options.add_experimental_option('prefs', preferences)
    browser_object = webdriver.Chrome(service=service, options=options)
    yield browser_object
    browser_object.quit()
