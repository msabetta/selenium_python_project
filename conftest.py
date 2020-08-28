#https://pytest-selenium.readthedocs.io/en/latest/index.html (for info)
import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="session")
def driver_get(request):
    wdr = webdriver.Chrome(r"./chromedriver/chromedriver.exe")
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"driver",wdr)
    yield
    request.addfinalizer(wdr.close)

@pytest.fixture(scope="class",params=["chrome","firefox"])
def driver_init(request):
    if request.param == "chrome":
        wdr = webdriver.Chrome(r"./chromedriver/chromedriver.exe")
    if request.param == "firefox":
        path_geckodriver = os.getcwd() + '\\geckodriver\\geckodriver.exe'
        os.environ['PATH'] += os.pathsep + path_geckodriver
        options = Options()
        options.headless = True
        wdr = webdriver.Firefox(options=options, executable_path=path_geckodriver)
    request.cls.driver = wdr
    yield
    request.addfinalizer(wdr.close)

def pytest_addoption(parser):
    parser.addoption("--wdropt", action="store", help="my option: chrome or firefox")

@pytest.fixture
def wdropt(request):
    return request.config.getoption("--wdropt")

def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item

def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" %previousfailed.name)
