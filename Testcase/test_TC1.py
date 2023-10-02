from POM.Login_Page import *
from POM.Home_Page import *
from Generic.Verify_Title import *

def test_TC1(launch):
     driver = launch
     verify_title(driver, "actiTIME - Login")
     l = LoginPage(driver)
     l.username("admin")
     l.password("manager")
     l.login()
     verify_title(driver,"actiTIME - Enter Time-Track")
     h = HomePage(driver)
     h.logout()
     

# // d={"apple":10,"mango":20}
# // d["mango"] ----> 20
#
# // d["fruit": {"apple":10,"mango":20}}
# // d["fruit"]["mango"] ----> 20