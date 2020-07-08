# CSVFileHandling
Reading CSV files and writing the data into separate Excel columns. Example included

Use this when needing to separate files in a folder with a given keyword that you are interested. In this case, we need to move all the files that contain the word "list" onto another folder. Use the code below once to separate the files. 

![alt text](https://github.com/cerdamario13/CSVFileHandling/blob/master/Images/movingFiles_code.PNG)


You will need to import shitil and os libraries. You only need to run this code once for our example. 

Next, we move into handling the CSV code. Normally all CSV code looks similar to the fromat below. 

CSVDATAImage HERE!!!!

We need to separate all the data into columns. there are also emoty data in the form of "<>". We can just count to see how many rows there are in order to avoid them or use a conditional statement to rule them out when gathering the data. 

Following that, we create the excelEditorFunction.py file. In here we have the main function that will do all the CSV data separation for us and we have the small for loops that help in the transition of CSV file to Excel file. We will need to impor the following libraries: csv, xlswriter, and os. 

functionCODEhere 

forloopcodehere!!

Lastly, we create excelEditor.py file that contains the for loop that will be used to read all of the files. I am sure that if can be done in a faster way but as of now that is how I know how to do it. I have included some files for practice. These contains multiple temperature readings at given time. 

for loop here!!!
