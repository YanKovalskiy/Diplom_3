# Проверь:

# всплывающее окно закрывается кликом по крестику,
# при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается,
# залогиненный пользователь может оформить заказ.

import allure


class TestBasicFunctionality:

    @allure.title('Проверка перехода по клику на ссылку «Конструктор» в шапке сайта')
    def test_goto_by_click_link_constructor(self, header, index_page):
        index_page.open_index_page()
        header.click_by_link_orders_feed()
        header.click_by_link_constructor()
        with allure.step(f'Проверяем текущий url (URL = {header.current_url})'):
            assert header.current_url == index_page.URL

    @allure.title('Проверка перехода по клику на ссылку «Лента заказов» в шапке сайта')
    def test_goto_by_click_link_orders_feed(self, header, index_page, order_feed_page):
        index_page.open_index_page()
        header.click_by_link_orders_feed()
        with allure.step(f'Проверяем текущий url (URL = {header.current_url})'):
            assert header.current_url == order_feed_page.URL

    @allure.title('Проверка появления всплывающего окно с деталями при кликнуть на ингредиент')
    def test_pop_up_details_window_by_click_on_ingredient(self, index_page):
        index_page.open_index_page()
        ingredient_name = index_page.get_name_ingredient_by_index_(0)
        index_page.click_on_ingredient_by_index_(0)
        with allure.step(f'Проверяем открылось ли окно с деталями об ингредиенте ({ingredient_name})'):
            assert index_page.get_ingredient_name_in_details_window() == ingredient_name

    @allure.title('Проверка закрытия всплывающего окна с деталями о ингредиенте кликом по крестику')
    def test_close_pop_up_details_window_by_click_on_cross_button(self, index_page):
        index_page.open_index_page()
        index_page.click_on_ingredient_by_index_(1)
        index_page.click_cross_button_in_details_window()



