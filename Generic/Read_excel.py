from xlrd import *

def read_locator(sheet):
     d = {}
     wb = open_workbook("../Excel/Locators.xlsx")
     sh = wb.sheet_by_name(sheet)
     row_count = sh.nrows
     for i in range(1, row_count):
          data = sh.row_values(i)
          d[data[0]] = (data[1], data[2])
     return d

# loc = read_locator("Home_Page")