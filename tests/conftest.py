import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def BrowserSetup(request):
    global driver
    global service_obj
    browser_name=request.config.getoption("--browser_name")
    if browser_name=="chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service_obj = Service("/Testing-20230705T115643Z-001/Python_notes/Python-Revised Topics/NewPythonclasses/driversfolder/chromedriver.exe")
        driver = webdriver.Chrome(options=options, service=service_obj)
    elif browser_name=="firefox":
        service_obj = Service("/Testing-20230705T115643Z-001/Python_notes/Python-Revised Topics/NewPythonclasses/driversfolder/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name=="edge":
        service_obj = Service("/Testing-20230705T115643Z-001/Python_notes/Python-Revised Topics/NewPythonclasses/driversfolder/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)

    driver.get("https://awesomeqa.com/ui/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    #driver.close()





