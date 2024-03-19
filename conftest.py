from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pytest import fixture


@fixture
def browser():
    browser_object = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser_object
    browser_object.quit()
