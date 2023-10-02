from selenium.webdriver.support.select import Select
from Generic.Read_excel import *
from Generic.Log_File import logg

loc = read_locator("Create_New_Tasks")

class CreatenewTasksPage:
     def __init__(self,driver):
          self.driver = driver
          
     def select_customer(self):
          logg("info", "select new customer option from drop down")
          dd = self.driver.find_element(*loc["select_customer"])
          s = Select(dd)
          s.select_by_visible_text("-- new customer --")
     
     def customername(self,data):
          logg("info", "entering customer name")
          self.driver.find_element(*loc["customername"]).send_keys(data)
          
     def projectname(self,data):
          logg("info", "entering project name")
          self.driver.find_element(*loc["projectname"]).send_keys(data)
          
     def taskname(self,data):
          logg("info", "entering task name")
          self.driver.find_element(*loc["taskname"]).send_keys(data)
          
     def create_tasks_button(self):
          ids = self.driver.window_handles
          logg("info", "clicking create task button")
          self.driver.find_element(*loc["create_tasks_button"]).click()
          self.driver.switch_to.window(ids[0])
          logg("info", "switching back to parent tab")