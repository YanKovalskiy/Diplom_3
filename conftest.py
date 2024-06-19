import pytest

from selenium import webdriver

from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from pages.account_profile_page import AccountProfilePage
from pages.account_order_history_page import AccountOrderHistoryPage
from pages.header import Header
from config import URL


@pytest.fixture()
def web_drv():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    yield driver

    driver.quit()


@pytest.fixture()
def login_page(web_drv):
    return LoginPage(web_drv)


@pytest.fixture()
def forgot_password_page(web_drv):
    return ForgotPasswordPage(web_drv)


@pytest.fixture()
def reset_password_page(web_drv):
    return ResetPasswordPage(web_drv)


@pytest.fixture()
def account_profile_page(web_drv):
    return AccountProfilePage(web_drv)


@pytest.fixture()
def account_order_history_page(web_drv):
    return AccountOrderHistoryPage(web_drv)


@pytest.fixture()
def header(web_drv):
    return Header(web_drv)


@pytest.fixture()
def login_details():
    return {
        'email': 'yankovskiy_8@gmail.com',
        'password': '123456'
    }
@pytest.fixture()
def logged(login_page, login_details):
    login_page.open_login_page()
    login_page.logining(login_details)
