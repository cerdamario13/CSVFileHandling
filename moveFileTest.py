# Moving files using python 
import shutil
import os

"""
Move files form one folder to another  --- ONLY NEED ONCE ---
"""
source = "/Users/PATH/Desktop/Cold Finger Temperature Data"
destination = "/Users/PATH/Desktop/ColdFingerData"

files = os.listdir(source)
key_word = "list"  # key word in files that we are interested in moving

# Counting how many files there are with a given name ("list" in this case)
list_cout = 0
with os.scandir(source) as dirs:
  for entry in dirs:
    if key_word in (entry.name):  # checking if the file contains a key word that we need ("list" in our case)
      #print(entry.name)
      list_cout += 1
# print(list_cout)  # prints list of files in folder path

# Moving all the files that contain "list" in the name
for file1 in files:
  if "list" in file1:
    new_path = shutil.move(f"{source}/{file1}", destination)  # don't need the way it was written, could be imporved and shortened
