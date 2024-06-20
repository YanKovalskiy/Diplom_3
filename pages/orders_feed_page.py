import allure

from pages.base_page import BasePage
from config import URL


class OrdersFeedPage(BasePage):
    def __init__(self, web_drv):
        super().__init__(web_drv)
        self.URL = f'{URL}/feed'

    def open_order_feed_page(self):
        with allure.step(f'Открываем страницу {self.URL}'):
            self.open_page(self.URL)
