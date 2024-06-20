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

    @allure.step('Ожидаем загрузки страницы')
    def wait_loading_page(self):
        self.wait_visible_element(IndexPageLocators.TAB_BUNS)

    @allure.step('Нажимаем на ингредиент')
    def click_on_ingredient_by_index_(self, index):
        self.get_visible_element_form_elements_by_index(IndexPageLocators.LIST_OF_INGREDIENTS, index).click()

    @allure.step('Получаем название ингредиента')
    def get_name_ingredient_by_index_(self, index):
        ingredient = self.get_visible_element_form_elements_by_index(IndexPageLocators.LIST_OF_INGREDIENTS, index)
        return ingredient.text.split('\n')[2]

    @allure.title('Нажимаем на крестик в окне с деталями о ингредиенте')
    def click_cross_button_in_details_window(self):
        self.click_by_element(IndexPageLocators.BUTTON_CROSS_IN_DETAILS_WINDOW)

    def get_ingredient_name_in_details_window(self):
        return self.get_visible_element(IndexPageLocators.NAME_INGREDIENT_IN_DETAILS_WINDOW).text
