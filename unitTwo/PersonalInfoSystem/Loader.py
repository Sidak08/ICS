'''
File: Loader.py
Name: Sidak Singh
Date: Nov 18, 2024

Description:
    This program recevies the name form the User Interface program and then open
    the specified file, reads it, and then sends the info contained in it back to
    the user interface program.

Function List:
    loadFile(filename):
        to open a txt file and return the text using a list
        pramaters:
            file name
        return:
            List of data within the file
'''
#===================================== Functions ==============================
from tkinter.constants import OUTSIDE


def loadFile(fileName):
    rFile = open(fileName, 'r')
    size = int(rFile.readline().strip())

    fileInfo = [None] * size

    for i in range(size):
        fileInfo[i] = rFile.readline().strip()

    rFile.close()
    return fileInfo

#==================================== Main Program ============================
output = loadFile("PersonalInfoFile.txt")
for i in range(len(output)):
    print(output[i])
