import allure

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from config import URL


class OrdersFeedPage(BasePage):
    def __init__(self, web_drv):
        super().__init__(web_drv)
        self.URL = f'{URL}/feed'

    def open_order_feed_page(self):
        with allure.step(f'Открываем страницу {self.URL}'):
            self.open_page(self.URL)

    @allure.step('Нажимаем на заказ')
    def click_orders_by_index_(self, index):
        orders = self.get_visible_elements(OrderFeedPageLocators.LIST_ORDERS)
        orders[index].click()

    @allure.step('Получаем номер заказа')
    def get_order_number_by_index(self, index):
        order_numbers = self.get_visible_elements(OrderFeedPageLocators.LIST_ORDER_NUMBERS)
        return order_numbers[index].text

    @allure.step("Получаем список номеров заказов из 'Ленты заказов'")
    def get_orders_number(self):
        orders_number = list(order_number.text for order_number in self.get_visible_elements(
            OrderFeedPageLocators.LIST_ORDER_NUMBERS))
        return orders_number

    @allure.step('Получаем номер заказа из всплывающего окна')
    def get_order_number_in_popup_window(self):
        return self.get_visible_element(OrderFeedPageLocators.ORDER_NUMBER_IN_POPUP_WINDOW).text
