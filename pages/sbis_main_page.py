from .base_page import BasePage
from .locators import SbisMainPageLocators


class SbisMainPage(BasePage):
    def should_be_contacts_section_link(self):
        assert self.is_element_present(*SbisMainPageLocators.CONTACTS_LINK), \
            'Contacts link is not presented'

    def go_to_contacts_section(self):
        self.browser.find_element(*SbisMainPageLocators.CONTACTS_LINK).click()
