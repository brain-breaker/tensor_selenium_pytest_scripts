from .pages.sbis_main_page import SbisMainPage
from .pages.sbis_download_page import SbisDownloadPage
from .pages.sbis_download_page import should_be_file_download, should_be_file_size_matched
from .pages.locators import SbisDownloadPageLocators
from pytest import mark
from time import sleep


@mark.checking_download
class TestDownloadFromMainPage:
    def test_user_can_go_to_download_link_and_download_the_plugin(self, browser):
        link = 'https://sbis.ru/'
        # user should see download link and can go to download link
        sbis_main_page = SbisMainPage(browser, link)
        sbis_main_page.open()
        sbis_main_page.should_be_download_link()
        sbis_main_page.go_to_download_link()
        # user should see plugin link and can go to plugin link
        sbis_download_page = SbisDownloadPage(browser, browser.current_url)
        sleep(2)
        sbis_download_page.should_be_plugin_link()
        sbis_download_page.go_to_plugin_link()
        # user should see web installer link and can download the plugin
        sbis_download_page.should_be_web_installer_link()
        correct_plugin_name = (
            browser.find_element(*SbisDownloadPageLocators.WEB_INSTALLER_LINK).get_attribute('href').split('/'))[-1]
        site_plugin_size = float(browser.find_element(*SbisDownloadPageLocators.WEB_INSTALLER_LINK).text.split()[2])
        sbis_download_page.go_to_plugin_download()
        # set the time to download the file (default = 10 sec)
        sleep(10)
        # user should see the plugin and its size should be matched that indicated on the site
        should_be_file_download(correct_plugin_name)
        should_be_file_size_matched(correct_plugin_name, site_plugin_size)
