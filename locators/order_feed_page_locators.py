from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    LIST_ORDERS = By.XPATH, "//*[contains(@class, 'OrderHistory_listItem')]"
    LIST_ORDER_NUMBERS = By.XPATH, "//*[contains(text(), '#')]"

    ORDER_NUMBER_IN_POPUP_WINDOW = By.XPATH, "//*[contains(@class, 'Modal_orderBox')]/p[1]"
