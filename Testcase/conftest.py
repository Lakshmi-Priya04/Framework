from selenium.webdriver import Chrome
import pytest
from Generic.Log_File import logg

@pytest.fixture(scope = "module")
def launch():
     driver = Chrome()
     logg("info", "launching browser")
     driver.get("http://localhost/login.do")
     driver.maximize_window()
     driver.implicitly_wait(10)
     yield driver
     driver.close()
     logg("info", "closing browser")