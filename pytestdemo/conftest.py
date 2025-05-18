import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
def pytest_addoption(parser):
    parser.addoption("--browser-name" ,action="store",default="chrome",help="browser selection")
@pytest.fixture(scope="function")
def browserinstances(request):
    browser_name=request.config.getoption("--browser-name")
    service_obj = Service()
    if browser_name=="chrome":
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name=="firefox":
        driver = webdriver.Firefox(service=service_obj)
    yield driver
