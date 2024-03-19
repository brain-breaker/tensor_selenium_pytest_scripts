from .base_page import BasePage
from .locators import TensorAboutPageLocators


class TensorAboutPage(BasePage):
    def checking_required_section_and_its_photo_attributes(self):
        self.should_be_required_section()
        self.should_be_the_same_attributes()

    def should_be_required_section(self):
        assert self.is_element_present(*TensorAboutPageLocators.REQUIRED_SECTION_NAME), \
            'Section is not presented'

    def should_be_the_same_attributes(self):
        # создаем словарь, где ключами будут искомые атрибуты, а в значениях пока пустые множества
        attributes_h_w = {'height': set(),
                          'width': set()}
        # проходим по каждому элементу с фотографией в блоке с ними и заносим соответственные атрибуты в наш словарь
        for element in self.browser.find_elements(*TensorAboutPageLocators.BLOCK_WITH_FOTO_LINK):
            attributes_h_w['height'].add(element.get_attribute('height'))
            attributes_h_w['width'].add(element.get_attribute('width'))
        # проверяем уникальность атрибутов благодаря свойствам множеств
        # если высота или ширина отличается у каких-то фото, то множества будут состоять больше, чем из 1 объекта
        # в случае не прохождения проверки увидим сообщение: The attributes are different!
        assert len(attributes_h_w['height']) == len(attributes_h_w['width']) == 1, \
            'The attributes are different!'
