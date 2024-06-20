from pages.base_page import BasePage
from config import URL


class AccountOrderHistoryPage(BasePage):
    def __init__(self, web_drv):
        super().__init__(web_drv)
        self.URL = f'{URL}/account/order-history'
