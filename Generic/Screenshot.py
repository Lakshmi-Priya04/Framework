from datetime import datetime
from selenium.webdriver import Chrome

def take_screenshot(driver):
     d = datetime.now().strftime("%d-%m-%y %H-%M-%S")
     driver.save_screenshot(f"../Screenshot/{d}.png")