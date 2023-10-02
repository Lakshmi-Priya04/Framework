from Generic.Screenshot import *
from time import sleep
def verify_text(driver,text):
     sleep(5)
     assert text in driver.page_source, take_screenshot(driver)