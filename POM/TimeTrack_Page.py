from Generic.Reading_Json import *
from time import sleep
from Generic.Log_File import logg

loc = read_json_locator()

class TimeTrackPage:
     def __init__(self,driver):
          self.driver = driver
     
     def select_user(self, user):
          logg("info", "selecting created user")
          self.driver.find_element(*loc["TimeTrack_Page"]["select_user"]).click()
          self.driver.find_element("xpath",f"//div[.='{user}']").click()
          sleep(5)
          # driver.find_element("xpath","//input[@id='ext-comp-1001']")
          
     def new_link(self):
          logg("info", "clicking new link")
          self.driver.find_element(*loc["TimeTrack_Page"]["new_link"]).click()
          ids = self.driver.window_handles
          self.driver.switch_to.window(ids[1])
     
     def enter_time(self, data):
          logg("info", "entering time")
          sleep(4)
          self.driver.find_element(*loc["TimeTrack_Page"]["enter_time"]).send_keys(data)
     
     def save_changes(self):
          logg("info", "click on save changes")
          self.driver.find_element(*loc["TimeTrack_Page"]["save_changes"]).click()
          sleep(4)