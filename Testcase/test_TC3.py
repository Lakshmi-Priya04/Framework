from POM.Login_Page import *
from POM.Home_Page import *
from Generic.Verify_Title import *
from POM.TimeTrack_Page import *
from POM.Create_New_Tasks import *
from Generic.Verify_text import *

def test_TC3(launch):
     driver = launch
     verify_title(driver, "actiTIME - Login")
     l = LoginPage(driver)
     l.username("admin")
     l.password("manager")
     l.login()
     verify_title(driver, "actiTIME - Enter Time-Track")
     h = HomePage(driver)
     h.timetrack_tab()
     verify_title(driver, "actiTIME - Enter Time-Track")
     t = TimeTrackPage(driver)
     t.select_user("Batch, Morning (MorningBatch)")
     t.new_link()
     c = CreatenewTasksPage(driver)
     c.select_customer()
     c.customername("selenium")
     c.projectname("automation")
     c.taskname("testscript")
     c.create_tasks_button()
     verify_text(driver,"testscript")
     h.logout()
     l = LoginPage(driver)
     l.username("MorningBatch")
     l.password("morning@1234")
     l.login()
     verify_title(driver, "actiTIME - Enter Time-Track")
     verify_text(driver,"testscript")
     t.enter_time("9")
     t.save_changes()
     h.logout()
     l.username("admin")
     l.password("manager")
     l.login()
     verify_title(driver, "actiTIME - Enter Time-Track")
     t.select_user("Batch, Morning (MorningBatch)")
     h.logout()