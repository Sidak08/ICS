'''
File: ExpressionLoad.py
Author: Dhenushan Ramesh
Date: Nov 30, 2024

Description:
This program recives a file name from the User Interface program and then opens
the specified text file, reads it and then send the info contained in it back to
the user Interface Program

Function list:

loadFile(filename)
    - function to open a txt file and load the info into a list
    - parameters needed: filename(has to be a string)
    - return: list with string data from the txt file

'''
#================ Functions ===================
def loadFile(fileName):
    """
    This function reads data from a file and returns it as a list.
    Parameters: fileName (str): The name of the file to read.
    Returns: list: A list containing the data from the file.
    """
    fileR = open(fileName,"r")  # Open the file for reading
    size = fileR.readline()  # uses the first line to see size of document
    size = int(size.strip())  # makes the size an int and removes any spaces/tabs
    fileInfo = [None]*size  # Create an empty list
    for i in range(size):
        fileInfo[i] = fileR.readline().strip()  # Read each line, remove spaces/tabs, and stores in the list
    fileR.close()  # Closes file
    return fileInfo  # Return the list with file data