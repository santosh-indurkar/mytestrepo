import pytest
#from selenium import webdriver
driver = None


#def pytest_addoption(parser):
#    parser.addoption(
#        "--browser_name", action="store", default="chrome", help="run all tests on given browser"
#    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
#    browser_name = request.config.getoption("browser_name")
#    print("USING BROWSER------------", browser_name)
    print("OPEN BROWSER")
 #   if browser_name == "chrome" or browser_name == "Chrome" or browser_name == "CHROME":
 #       driver = webdriver.Chrome()
 #   elif browser_name == "firefox" or browser_name == "Firefox" or browser_name == "FIREFOX" or browser_name == "FireFox":
 #       driver = webdriver.Firefox()
 
 #   driver.maximize_window()
 #   request.cls.driver = driver
    yield
    print("CLOSE BROWSER")
 #   driver.close()
