import allure

from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators
from config import URL


class ResetPasswordPage(BasePage):
    RESET_PASSWORD_PAGE_URL = f'{URL}/reset-password'

    @property
    def inactive_border_of_field_password(self):
        return self.get_visible_element(ResetPasswordLocators.INACTIVE_BORDER_FIELD_PASSWORD)

    @allure.step('Ожидаем загрузку страницы')
    def wait_load_page(self):
        self.wait_visible_element(ResetPasswordLocators.ICON_IN_FIELD_PASSWORD)

    @allure.step('Нажимаем на иконку скрыть/показать пароль')
    def click_icon_in_field_password(self):
        self.click_by_element(ResetPasswordLocators.ICON_IN_FIELD_PASSWORD)

