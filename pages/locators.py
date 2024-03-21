from selenium.webdriver.common.by import By


class SbisMainPageLocators:
    CONTACTS_LINK = (By.CSS_SELECTOR, 'a.sbisru-Header__menu-link[href="/contacts"]')
    DOWNLOAD_LINK = (By.CSS_SELECTOR, 'a.sbisru-Footer__link[href="/download"]')


class SbisContactsPageLocators:
    TENSOR_BANNER_LINK = (By.CLASS_NAME, 'sbisru-Contacts__logo-tensor.mb-12')
    REGION_LINK = (By.CSS_SELECTOR, 'div.sbisru-Contacts .sbis_ru-Region-Chooser__text')
    PARTNER_LIST = (By.CLASS_NAME, 'sbisru-Contacts-List__col')
    PARTNER_LIST_CITY = (By.ID, 'city-id-2')
    PARTNER_NAME = (By.CLASS_NAME, 'sbisru-Contacts-List__name')
    CHOOSE_REGION_LINK = (By.XPATH, '//*[contains(text(), "Камчатский край")]')


class SbisDownloadPageLocators:
    PLUGIN_LINK = (By.CSS_SELECTOR, '[data-id="plugin"]')
    WEB_INSTALLER_LINK = (By.PARTIAL_LINK_TEXT, 'Exe')


class TensorMainPageLocators:
    REQUIRED_BLOCK_NAME = (By.XPATH, '//*[text()="Сила в людях"]')
    MORE_DETAILES_LINK = (By.CSS_SELECTOR, 'a.tensor_ru-link[href="/about"]')


class TensorAboutPageLocators:
    REQUIRED_SECTION_NAME = (By.XPATH, '//*[text()="Работаем"]')
    BLOCK_WITH_FOTO_LINK = (By.CSS_SELECTOR, 'div.tensor_ru-About__block3-image-wrapper img')
