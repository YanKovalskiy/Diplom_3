from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as WDWait


class BasePage:
    DEFAULT_TIMEOUT = 10

    def __init__(self, web_drv):
        self.web_drv = web_drv

    @property
    def current_url(self):
        return self.web_drv.current_url

    def open_page(self, url):
        self.web_drv.get(url)

    def click_by_element(self, locator, timeout=DEFAULT_TIMEOUT):
        WDWait(self.web_drv, timeout).until(ec.element_to_be_clickable(locator)).click()

    def fill_field(self, locator, text, timeout=DEFAULT_TIMEOUT):
        WDWait(self.web_drv, timeout).until(ec.element_to_be_clickable(locator)).send_keys(text)

    def wait_visible_element(self, locator, timeout=DEFAULT_TIMEOUT):
        WDWait(self.web_drv, timeout).until(ec.visibility_of_element_located(locator))

    def wait_invisibility_element(self, locator, timeout=DEFAULT_TIMEOUT):
        WDWait(self.web_drv, timeout).until(ec.invisibility_of_element(locator))

    def get_attribute_element(self, locator, attribute, timeout=DEFAULT_TIMEOUT):
        return WDWait(self.web_drv, timeout).until(ec.visibility_of_element_located(locator)).get_attribute(attribute)

    def get_visible_element(self,  locator, timeout=DEFAULT_TIMEOUT):
        return WDWait(self.web_drv, timeout).until((ec.visibility_of_element_located(locator)))

    def get_visible_element_form_elements_by_index(self, locator, index, timeout=DEFAULT_TIMEOUT):
        elements_list = WDWait(self.web_drv, timeout).until((ec.visibility_of_all_elements_located(locator)))
        # elements_list = self.web_drv.find_elements(*locator)
        return elements_list[index]
