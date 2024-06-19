import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from config import URL


class LoginPage(BasePage):
    LOGIN_PAGE_URL = f'{URL}/login'

    @allure.step(f'Открываем страницу {LOGIN_PAGE_URL}')
    def open_login_page(self):
        self.open_page(self.LOGIN_PAGE_URL)

    @allure.step('Ожидаем загрузки страницы')
    def wait_loading_page(self):
        self.wait_visible_element(LoginPageLocators.BUTTON_ENTER)

    @allure.step("Нажимаем на ссылку 'Восстановить пароль'")
    def click_link_recovery_password(self):
        self.click_by_element(LoginPageLocators.LINK_RECOVERY_PASSWORD)

    @allure.step("Заполняем поле 'E-mail'")
    def fill_email_field(self, email):
        self.fill_field(LoginPageLocators.INPUT_FIELD_EMAIL, email)

    @allure.step("Заполняем поле 'Password'")
    def fill_password_field(self, password):
        self.fill_field(LoginPageLocators.INPUT_FIELD_PASSWORD, password)

    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_button_enter(self):
        self.click_by_element(LoginPageLocators.BUTTON_ENTER)

    @allure.step("Логинимся в системе")
    def logining(self, login_details):
        self.fill_email_field(login_details['email'])
        self.fill_password_field(login_details['password'])
        self.click_button_enter()

