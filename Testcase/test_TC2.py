from POM.Login_Page import *
from POM.Home_Page import *
from Generic.Verify_Title import *
from POM.Userlist_Page import *
from Generic.Verify_text import *

def test_TC2(launch):
     driver = launch
     verify_title(driver, "actiTIME - Login")
     l = LoginPage(driver)
     l.username("admin")
     l.password("manager")
     l.login()
     verify_title(driver, "actiTIME - Enter Time-Track")
     h = HomePage(driver)
     h.user_tab()
     verify_title(driver, "actiTIME - User List")
     u = UserlistPage(driver)
     u.user_button()
     verify_text(driver, "Create New User")
     u.firstname("Morning")
     u.lastname("Batch")
     u.email("morning@gmail.com")
     u.username("MorningBatch")
     u.password("morning@1234")
     u.retype_password("morning@1234")
     u.create_user_button()
     verify_text(driver, "Batch, Morning (MorningBatch)")
     h.logout()
     l = LoginPage(driver)
     l.username("MorningBatch")
     l.password("morning@1234")
     l.login()
     verify_title(driver, "actiTIME - Enter Time-Track")
     h.logout()