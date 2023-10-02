from Generic.Read_excel import *
from Generic.Log_File import *
from Generic.Verify_Title import *
loc = read_locator("Home_Page")

class HomePage:
     def __init__(self,driver):
          self.driver = driver
          
     def logout(self):
          logg("info", "clicking logout button")
          self.driver.find_element(*loc["logout"]).click()
          verify_title(self.driver, "actiTIME - Login")
          
     def user_tab(self):
          logg("info", "clicking user tab")
          self.driver.find_element(*loc["user_tab"]).click()
     
     def timetrack_tab(self):
          logg("info", "clicking timetrack tab")
          self.driver.find_element(*loc["timetrack_tab"]).click()