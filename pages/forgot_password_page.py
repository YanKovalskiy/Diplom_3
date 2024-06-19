from pages.base_page import BasePage
from config import URL


class ForgotPasswordPage(BasePage):
    FORGOT_PASSWORD_PAGE_URL = f'{URL}/forgot-password'
