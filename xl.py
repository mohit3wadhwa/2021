import openpyxl
import tkinter
# To open the workbook  
# workbook object is created 
wb_obj = openpyxl.load_workbook("test.xlsx") 
  
# Get workbook active sheet object 
# from the active attribute 
sheet_obj = wb_obj.active 
  
# Cell objects also have a row, column,  
# and coordinate attributes that provide 
# location information for the cell. 
  
# Note: The first row or  
# column integer is 1, not 0. 
  
# Cell object is created by using  
# sheet object's cell() method. 
cell_obj = sheet_obj.cell(row = 3, column = 2) 
  
# Print value of cell object  
# using the value attribute 
print(cell_obj.value) 