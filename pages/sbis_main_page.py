from .base_page import BasePage
from .locators import SbisMainPageLocators


class SbisMainPage(BasePage):
    def should_be_contacts_section_link(self):
        assert self.is_element_present(*SbisMainPageLocators.CONTACTS_LINK), \
            'Contacts link is not presented'

    def go_to_contacts_section(self):
        self.browser.find_element(*SbisMainPageLocators.CONTACTS_LINK).click()

    def should_be_download_link(self):
        assert self.is_element_present(*SbisMainPageLocators.DOWNLOAD_LINK), \
            'Download link is not presented'

    def go_to_download_link(self):
        download_footer = self.browser.find_element(*SbisMainPageLocators.DOWNLOAD_LINK)
        # скролл до нужного элемента, чтобы он точно стал видимым
        self.browser.execute_script('return arguments[0].scrollIntoView(true);', download_footer)
        # теперь перекрытия элемента не будет и можем кликать
        download_footer.click()
