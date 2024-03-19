from .pages.sbis_main_page import SbisMainPage
from .pages.sbis_contacts_page import SbisContactsPage
from .pages.tensor_main_page import TensorMainPage
from .pages.tensor_about_page import TensorAboutPage
from pytest import mark


@mark.checking_attributes
class TestAttributesFotoFromMainPage:
    def test_user_can_go_to_required_section_and_checking_attributes(self, browser):
        link = 'https://sbis.ru/'
        # user should see contacts link and can go to contacts
        sbis_main_page = SbisMainPage(browser, link)
        sbis_main_page.open()
        sbis_main_page.should_be_contacts_section_link()
        sbis_main_page.go_to_contacts_section()
        # user should see tensor banner link and can go to tensor banner
        sbis_contacts_page = SbisContactsPage(browser, browser.current_url)
        sbis_contacts_page.should_be_tensor_banner_link()
        sbis_contacts_page.go_to_tensor_banner()
        # need to switch to a new tab, because the link will open in a new window
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)
        # user should see required block and more details link
        tensor_main_page = TensorMainPage(browser, browser.current_url)
        tensor_main_page.checking_required_block_and_go_to_more_details()
        # user should see required section and checking attributes
        tensor_about_page = TensorAboutPage(browser, browser.current_url)
        tensor_about_page.checking_required_section_and_its_photo_attributes()
