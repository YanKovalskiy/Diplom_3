import allure

from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators
from config import URL


class ForgotPasswordPage(BasePage):
    FORGOT_PASSWORD_PAGE_URL = f'{URL}/forgot-password'

    @allure.step(f'Открываем страницу {FORGOT_PASSWORD_PAGE_URL}')
    def open_forgot_password_page(self):
        self.open_page(self.FORGOT_PASSWORD_PAGE_URL)

    @allure.step("Заполняем поле 'E-mail'")
    def fill_email_field(self, email):
        self.fill_field(ForgotPasswordLocators.INPUT_FIELD_EMAIL, email)

    @allure.step("Нажимаем кнопку 'Восстановить'")
    def click_button_recovery(self):
        self.click_by_element(ForgotPasswordLocators.BUTTON_RECOVERY)
