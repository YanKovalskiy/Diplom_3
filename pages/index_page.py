import allure

from pages.base_page import BasePage
from locators.index_page_locators import IndexPageLocators
from config import URL


class IndexPage(BasePage):
    def __init__(self, web_drv):
        super().__init__(web_drv)
        self.URL = f'{URL}/'

    def open_index_page(self):
        with allure.step(f'Открываем страницу {self.URL}'):
            self.open_page(self.URL)

    @allure.step('Нажимаем на ингредиент')
    def click_on_ingredient_by_index_(self, index):
        self.get_visible_element_form_elements_by_index(IndexPageLocators.LIST_OF_INGREDIENTS, index).click()

    @allure.step('Нажимаем на крестик в окне с деталями о ингредиенте')
    def click_cross_button_in_details_window(self):
        self.click_by_element(IndexPageLocators.BUTTON_CROSS_IN_DETAILS_WINDOW)

    @allure.step("Нажимаем на кнопку 'Оформить заказ'")
    def click_button_place_order(self):
        self.click_by_element(IndexPageLocators.BUTTON_PLACE_ORDER)

    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient_to_order_by_index(self, index):
        ingredient = self.get_visible_element_form_elements_by_index(IndexPageLocators.LIST_OF_INGREDIENTS, index)
        basket = self.get_visible_element(IndexPageLocators.SECTION_CONSTRUCTOR_BASKET)
        self.drag_and_drop(ingredient, basket)

    @allure.step('Получаем название ингредиента')
    def get_name_ingredient_by_index_(self, index):
        ingredient = self.get_visible_element_form_elements_by_index(IndexPageLocators.LIST_OF_INGREDIENTS, index)
        return ingredient.text.split('\n')[2]

    @allure.step('Получаем название ингредиента в окне с деталями')
    def get_ingredient_name_in_details_window(self):
        return self.get_visible_element(IndexPageLocators.TEXT_NAME_INGREDIENT_IN_DETAILS_WINDOW).text

    @allure.step('Получаем текст из окна подтверждения заказа')
    def get_text_fom_order_confirm_window(self):
        return self.get_visible_element(IndexPageLocators.TEXT_ORDER_START_TO_PREPARE).text

    @allure.step("Получаем web-элемент pop-up окно 'Детали ингредиента'")
    def get_popup_details_window(self):
        return self.get_visible_element(IndexPageLocators.MODAL_POPUP_WINDOW)

    @allure.step('Получаем значение счетчика ингредиента')
    def get_counter_ingredient_by_index_(self, index):
        counter = self.get_visible_element_form_elements_by_index(IndexPageLocators.LIST_COUNTERS_OF_INGREDIENTS, index)
        return int(counter.text)
