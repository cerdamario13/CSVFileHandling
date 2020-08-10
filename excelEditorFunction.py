import numpy as np
import csv
import xlsxwriter
import os

# Use these to test the function before using a for loop (optional) or use the files provided for practice
name = 'cerda'
source1 = f"/Users/{name}/Desktop/ColdFingerData/06262020list.csv" # the file we are editing
newFileName1 = f"/Users/{name}/Desktop/ColdFingerData_Filtered/TEST.xlsx" # the file that is edited ALREADY

# Function that reads CSV files and writes the data into excel format
def fileEditor(source, newFileName):
  time = []  # Inititating the arrays (Determine how many arrays are needed)
  temp_rack =  []
  temp_fing =  []
  temp_rack2 =  []
  temp_fing2 =  []
  with open(source) as File:  # Open the CSV file
      reader = csv.reader(File, delimiter=';')
      for row in reader:
        time.append(row[0])  # Append the data into separated arrays
        temp_rack.append(row[1])
        temp_fing.append(row[2])
        temp_rack2.append(row[13])  # since se have several empty columns of data, we skip to the desired data columns
        temp_fing2.append(row[14])
  a = [time, temp_rack, temp_fing, temp_rack2, temp_fing2]  # array that contains all the CSV columns in one array

  wb = xlsxwriter.Workbook(newFileName)  # Create a new Excel file 
  ws = wb.add_worksheet()
  row = 0
  col = 0
  for i in range(len(a)):  # Write all the data into separate columns
    for i2 in range(len(a[0])):
      ws.write(row, col, a[i][i2])
      row += 1
    col += 1
    row = 0
  wb.close()  # closing the workbook

# fileEditor(source1, newFileName1)  # Testing the function with only one file
# print("PASS")

"""
Gathering all the file names in the folder and removing the "list.csv" --- ONLY NEED THIS ONCE ---
"""
path = r"C:/Users/cerda/Desktop/ColdFingerData"
# Call listdir() - Path is a directory of which you want to list
directories = os.listdir(path)
# Need a way to remove the (list.csv) from tall of the names
short_name_list = directories
list_remove_name = []
for r in short_name_list:
  list_remove_name.append(r.replace('list.csv', '.xlsx'))  # removes "list.csv" and replaces it with " "
# print(list_remove_name)

# New filed path for edited files (once they run through excel_writer function)
edited_files_path = np.array([])
for new_paths in list_remove_name:
  edited_files_path = np.append(edited_files_path, f"/Users/{name}/Desktop/ColdFingerData_Filtered/{new_paths}")

# Making a list of all the filed in the folder path
unedited_csv_files_path = np.array([])
for paths in directories:
  unedited_csv_files_path = np.append(unedited_csv_files_path, f"/Users/{name}/Desktop/ColdFingerData/{paths}")

