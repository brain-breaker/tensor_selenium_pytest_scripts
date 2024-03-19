from .base_page import BasePage
from .locators import SbisContactsPageLocators


class SbisContactsPage(BasePage):
    def should_be_tensor_banner_link(self):
        assert self.is_element_present(*SbisContactsPageLocators.TENSOR_BANNER_LINK), \
            'Tensor link is not presented'

    def go_to_tensor_banner(self):
        self.browser.find_element(*SbisContactsPageLocators.TENSOR_BANNER_LINK).click()

    def should_be_region_link(self):
        assert self.is_element_present(*SbisContactsPageLocators.REGION_LINK), \
            'Region link is not presented'

    def should_be_partner_list(self):
        assert self.is_element_present(*SbisContactsPageLocators.PARTNER_LIST), \
            'Partner list is not presented'

    def should_be_correct_our_region(self, correct_our_region):
        assert (correct_our_region in
                self.browser.find_element(*SbisContactsPageLocators.REGION_LINK).text), \
            'Our region is not correct'

    def should_be_correct_our_partner_list_city(self, correct_our_partner_list_city):
        assert (correct_our_partner_list_city in
                self.browser.find_element(*SbisContactsPageLocators.PARTNER_LIST_CITY).text), \
            'Our list city is not correct'

    def should_be_correct_our_partner_name(self, correct_our_partner_name):
        assert (correct_our_partner_name in
                self.browser.find_element(*SbisContactsPageLocators.PARTNER_NAME).text), \
            'Our partner name is not correct'

    def go_to_region_link(self):
        self.browser.find_element(*SbisContactsPageLocators.REGION_LINK).click()

    def go_to_choose_region_link(self):
        self.browser.find_element(*SbisContactsPageLocators.CHOOSE_REGION_LINK).click()

    def should_be_correct_selected_region(self, correct_selected_region):
        assert (correct_selected_region in
                self.browser.find_element(*SbisContactsPageLocators.REGION_LINK).text), \
            'The selected region is not correct'

    def should_be_correct_selected_partner_list_city(self, correct_selected_partner_list_city):
        assert (correct_selected_partner_list_city in
                self.browser.find_element(*SbisContactsPageLocators.PARTNER_LIST_CITY).text), \
            'The selected partner list city is not correct'

    def should_be_correct_selected_partner_name(self, correct_selected_partner_name):
        assert (correct_selected_partner_name in
                self.browser.find_element(*SbisContactsPageLocators.PARTNER_NAME).text), \
            'The selected partner name is not correct'

    def should_be_correct_selected_region_url(self, correct_selected_region_number):
        assert correct_selected_region_number in self.browser.current_url, \
            'The selected region URL is not correct'

    def should_be_correct_selected_region_title(self, correct_selected_region):
        assert correct_selected_region in self.browser.title, \
            'The selected region title is not correct'
