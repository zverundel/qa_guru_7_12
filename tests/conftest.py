import allure
from selene import browser
import pytest


@allure.step("Настройка рзмера окна браузера")
@pytest.fixture
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@allure.step("Отрытие сайта")
@pytest.fixture
def browser_open_url(browser_size):
    browser.config.base_url = 'https://demoqa.com'