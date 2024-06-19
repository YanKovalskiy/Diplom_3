import pytest
from selenium import webdriver
from config import URL


@pytest.fixture()
def web_drv():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    yield driver

    driver.quit()