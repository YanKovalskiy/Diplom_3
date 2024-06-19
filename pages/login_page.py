import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from config import URL


class LoginPage(BasePage):
    LOGIN_PAGE_URL = f'{URL}/login'

    @allure.step(f'Открываем страницу {LOGIN_PAGE_URL}')
    def open_login_page(self):
        self.open_page(self.LOGIN_PAGE_URL)

    @allure.step("Нажимаем на ссылку 'Восстановить пароль'")
    def click_link_recovery_password(self):
        self.click_by_element(LoginPageLocators.LINK_RECOVERY_PASSWORD)
