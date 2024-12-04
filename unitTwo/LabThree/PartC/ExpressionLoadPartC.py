'''
File: Loader.py
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
    fileR = open(fileName,"r")
    size = fileR.readline()
    size = int(size.strip())
    fileInfo = [None]*size
    for i in range(size):
        fileInfo[i] = fileR.readline().strip() 
    fileR.close()
    return fileInfo

def saveResults(fileInfo):
    fileW = open("Questionswithanswers", "w")
    for i in range (len(fileInfo)):
        fileW.write(fileInfo[i])
    fileW.close