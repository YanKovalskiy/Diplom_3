from pages.base_page import BasePage
from config import URL


class AccountOrderHistoryPage(BasePage):
    ACCOUNT_ORDER_HISTORY_PAGE_URL = f'{URL}/account/order-history'
