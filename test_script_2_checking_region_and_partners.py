from .pages.sbis_main_page import SbisMainPage
from .pages.sbis_contacts_page import SbisContactsPage
from .pages.locators import SbisContactsPageLocators
from pytest import mark
from time import sleep


@mark.checking_region
class TestRegionFromMainPage:
    def test_user_can_go_to_region_link_and_checking_partners(self, browser):
        link = 'https://sbis.ru/'
        # user should see contacts link and can go to contacts
        sbis_main_page = SbisMainPage(browser, link)
        sbis_main_page.open()
        sbis_main_page.should_be_contacts_section_link()
        sbis_main_page.go_to_contacts_section()
        # user should see region link and partner list
        sbis_contacts_page = SbisContactsPage(browser, browser.current_url)
        sbis_contacts_page.should_be_region_link()
        sbis_contacts_page.should_be_partner_list()
        our_region = 'Ярославская обл.'
        our_partner_city = 'Ярославль'
        our_partner_name = 'СБИС - Ярославль'
        sbis_contacts_page.should_be_correct_our_region(our_region)
        sbis_contacts_page.should_be_correct_our_partner_list_city(our_partner_city)
        sbis_contacts_page.should_be_correct_our_partner_name(our_partner_name)
        # user can go to region link and choose region
        sbis_contacts_page.go_to_region_link()
        selected_region = ' '.join(browser.find_element(*SbisContactsPageLocators.CHOOSE_REGION_LINK).text.split()[1:])
        selected_region_number = browser.find_element(*SbisContactsPageLocators.CHOOSE_REGION_LINK).text.split()[0]
        sleep(1)
        sbis_contacts_page.go_to_choose_region_link()
        sleep(1)
        # user should see the selected region, its partner list, url and title
        selected_partner_list_city = 'Петропавловск-Камчатский'
        selected_partner_name = 'СБИС - Камчатка'
        sbis_contacts_page.should_be_correct_selected_region(selected_region)
        sbis_contacts_page.should_be_correct_selected_partner_list_city(selected_partner_list_city)
        sbis_contacts_page.should_be_correct_selected_partner_name(selected_partner_name)
        sbis_contacts_page.should_be_correct_selected_region_url(selected_region_number)
        sbis_contacts_page.should_be_correct_selected_region_title(selected_region)
