from Generic.Reading_Json import *
from Generic.Log_File import *

loc = read_json_locator()

class LoginPage:
     def __init__(self,driver):
          self.driver = driver

     def username(self,data):
          logg("info", "entering username")
          self.driver.find_element(*loc["Login_Page"]["username"]).send_keys(data)

     def password(self,data):
          logg("info", "entering password")
          self.driver.find_element(*loc["Login_Page"]["password"]).send_keys(data)

     def login(self):
          logg("info", "clicking login button")
          self.driver.find_element(*loc["Login_Page"]["login"]).click()

# l=[10,20]
# print(l)       #[10, 20]
# print(*l)      #10 20  (unpacking)