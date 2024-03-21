from .base_page import BasePage
from .locators import SbisDownloadPageLocators
from os import path
from pathlib import Path


def should_be_file_download(file_name):
    cwd = Path.cwd()
    assert path.isfile(file_name) and not set(cwd.glob('*.crdownload')), \
        'The file did not download'


def should_be_file_size_matched(file_name, site_file_size):
    file_size_mb = round(path.getsize(file_name) / (1024 * 1024), 2)
    assert file_size_mb == round(site_file_size, 2), \
        f'The file size {file_size_mb} does not match indicated {site_file_size}'


class SbisDownloadPage(BasePage):
    def should_be_plugin_link(self):
        assert self.is_element_present(*SbisDownloadPageLocators.PLUGIN_LINK), \
            'Plugin link is not presented'

    def go_to_plugin_link(self):
        self.browser.find_element(*SbisDownloadPageLocators.PLUGIN_LINK).click()

    def should_be_web_installer_link(self):
        assert self.is_element_present(*SbisDownloadPageLocators.WEB_INSTALLER_LINK), \
            'Web installer link is not presented'

    def go_to_plugin_download(self):
        self.browser.find_element(*SbisDownloadPageLocators.WEB_INSTALLER_LINK).click()
