import pytest

from selenium import webdriver

from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
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
