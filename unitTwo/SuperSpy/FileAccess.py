'''
File: ExpressionLoadPartC.py
Author: Dhenushan Ramesh
Date: Dec 9, 2024

Description:
This program recives a file name from the User Interface program and then opens
the specified text file, reads it and then send the info contained in it back to
the user Interface Program

Function list:

loadFile(filename)
    - function to open a txt file and load the info into a list
    - parameters needed: filename(has to be a string)
    - return: list with string data from the txt file

saveResults(fileInfo)
    - function to save results into a new file
    - parameters needed: fileInfo
    - return: does not return anything
'''
#================ Functions ===================

def loadFile(fileName):
    fileR = open(fileName,"r") 
    size = fileR.readline()  # uses the first line to see size of document
    size = int(size.strip())  # makes the size an int and removes any spaces/tabs
    fileInfo = [None]*size  # Create an empty list
    for i in range(size):
        fileInfo[i] = fileR.readline().strip()  # Read each line, remove spaces/tabs, and stores in the list
    fileR.close()
    return fileInfo  # Return the list with file data

def saveResults(fileInfo):
    fileW = open("QuestionsWithAnswers.txt", "w") # Open a file called "QuestionsWithAnswers.txt" in write mode
    for i in range(len(fileInfo)):  # looks through each items in the list
        fileW.write(fileInfo[i])  # Write each item into the file
    fileW.close()

