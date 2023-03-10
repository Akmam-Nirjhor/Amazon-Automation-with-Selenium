import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name =request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("https://www.amazon.com/ ")
        driver.maximize_window()
    request.cls.driver = driver
    yield


