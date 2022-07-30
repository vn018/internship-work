# -*- coding: utf-8 -*-
"""Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UVeP_P5Wf90111EDn9Y74dmEcsQiZJvu
"""

!pip install xlsxwriter
!pip install pycountry
!pip install countryinfo

# Book1.xlsm is a blank excel file which is imported here to add macros to the xlsxwriter file
! vba_extract.py Reference.xlsm

import xlsxwriter
import pycountry
from countryinfo import CountryInfo
from google.colab import files
import xlrd
import openpyxl

# Create workbook and worksheet
workbook = xlsxwriter.Workbook('task1.xlsm')
worksheet = workbook.add_worksheet()

#adding a VBA project file extracted from an existing xlsm file
workbook.add_vba_project('./vbaProject.bin')

# Setting header, column and row formats
header_format = workbook.add_format({
    'border': 1,
    'bg_color': '#C6EFCE',
    'bold': True,
    'text_wrap': True,
    'valign': 'vcenter',
    'indent': 2,
})

worksheet.set_column(0,300,30)
worksheet.set_row(0, 36)


heading1 = 'Countries'
worksheet.write('A1', heading1, header_format)
heading2 = 'States'
worksheet.write('B1', heading2, header_format)
heading3 = 'Dropdown Data - Countries'
worksheet.write('Y1',heading3 , header_format)

# Appending country names and IDs to a list
countries = []
for x in pycountry.countries:
  countries.append(x.name + ' - ' + x.alpha_2)

# Writing the contents of the above list to the cells in the column Y
worksheet.write_column('Y2', countries)

col_num = 27
for x in pycountry.countries:
  heading = str(x.name) + ' - ' + str(x.alpha_2)                 
  worksheet.write(0,col_num, heading , header_format)             # Writing name and ID of each country as heading at the first cell of a column starting from
                                                                  # column AB
  states = []
  for y in pycountry.subdivisions:
    if(y.country.name == x.name):  
      states.append(y.name)                                       # Appending names of states/provinces of a country to a list
  worksheet.write_column(1, col_num, states)                      # Writing the names of states of a country in the column on which its name is given as heading
  col_num += 1

# Adding data validation property to cells of column A from 2nd row to 30th row
# Source of the values in the dropdown list is the country names stored in column Y
worksheet.data_validation('A2:A30', {'validate' : 'list', 'source': '=$Y$2:$Y$250'})
for i in range(29):
  # For each cell to the write of a cell in column A, drop down list of the country selected in column A is created
  # Source of values selected by matching the name of country in column A
  # to the heading of one of the columns from AB to JP(which have names of states of each country)
  worksheet.data_validation('B'+str(2+i) ,{'validate' : 'list', 'source': '=INDEX($AB$3:$JP$250, 0, MATCH($A$'+str(2+i)+', $AB$1:$JP$1, 0))'})

workbook.close()

# Download the excel file
files.download('task1.xlsm')