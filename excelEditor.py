
import csv
import xlsxwriter
from excelEditorFunction import edited_files_path, unedited_csv_files_path, fileEditor
import time


# Use for loop to read and write multiple files.  
for x, y in zip(unedited_csv_files_path, edited_files_path):
  fileEditor(x, y)
print("PASS")



