# Проверь:
#
# при создании нового заказа счётчик Выполнено за всё время увеличивается,
# при создании нового заказа счётчик Выполнено за сегодня увеличивается,
# после оформления заказа его номер появляется в разделе В работе.
import allure
import pytest


class TestSectionOrderFeed:

    @allure.title('Проверка открытия всплывающее окна с деталями по клику на заказ в ленте заказов')
    def test_opening_popup_window_by_click_on_order(self, order_feed_page):
        order_index = 0
        order_feed_page.open_order_feed_page()
        number_order = order_feed_page.get_order_number_by_index(order_index)
        order_feed_page.click_orders_by_index_(order_index)
        with allure.step('проверяем, что окно заказа открылось'):
            assert order_feed_page.get_order_number_in_popup_window() == number_order

    @allure.title("Проверка отображения заказов пользователя из раздела 'История заказов' на странице 'Лента заказов'")
    @pytest.mark.orders_count(2)
    def test_displaying_user_orders_from_order_history_section_on_order_feed_page(self, user, logged,
                                                                                  order, header, order_feed_page,
                                                                                  account_profile_page,
                                                                                  account_order_history_page):
        header.click_by_link_personal_account()
        account_profile_page.click_link_order_history()
        order_numbers_from_order_history = account_order_history_page.get_order_numbers()
        order_feed_page.open_order_feed_page()
        order_numbers_from_order_feed = order_feed_page.get_orders_number()
        for order_number in order_numbers_from_order_history:
            with allure.step(f"Проверяем есть ли заказ {order_number} в 'Ленте заказов'"):
                assert order_number in order_numbers_from_order_feed
