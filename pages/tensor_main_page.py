from .base_page import BasePage
from .locators import TensorMainPageLocators


class TensorMainPage(BasePage):
    def checking_required_block_and_go_to_more_details(self):
        self.should_be_required_block()
        self.should_be_more_details_link()
        self.go_to_more_details_link()

    def should_be_required_block(self):
        assert self.is_element_present(*TensorMainPageLocators.REQUIRED_BLOCK_NAME), \
            'Block is not presented'

    def should_be_more_details_link(self):
        assert self.is_element_present(*TensorMainPageLocators.MORE_DETAILES_LINK), \
            'Link More details is not presented'

    def go_to_more_details_link(self):
        more_details = self.browser.find_element(*TensorMainPageLocators.MORE_DETAILES_LINK)
        # скролл до нужного элемента, чтобы он точно стал видимым
        self.browser.execute_script('return arguments[0].scrollIntoView(true);', more_details)
        # теперь перекрытия элемента не будет и можем кликать
        more_details.click()
