from Generic.Read_excel import *

loc = read_locator("Userlist_Page")

class UserlistPage:
     def __init__(self,driver):
          self.driver = driver
          
     def user_button(self):
          self.driver.find_element(*loc["user_button"]).click()
          
     def firstname(self,data):
          self.driver.find_element(*loc["firstname"]).send_keys(data)
          
     def lastname(self,data):
          self.driver.find_element(*loc["lastname"]).send_keys(data)
          
     def email(self,data):
          self.driver.find_element(*loc["email"]).send_keys(data)
          
     def username(self,data):
          self.driver.find_element(*loc["username"]).send_keys(data)
          
     def password(self,data):
          self.driver.find_element(*loc["password"]).send_keys(data)
          
     def retype_password(self,data):
          self.driver.find_element(*loc["retype_password"]).send_keys(data)
     
     def create_user_button(self):
          self.driver.find_element(*loc["create_user_button"]).click()