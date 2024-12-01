#Denu
'''
File: Loader.py
Author: Dhenushan Ramesh
Date: Nov 30, 2024

Description:
This program recives a file name from the User Interface program and then opens
the specified text file, reads it and then send the info contained in it back to
the user Interface Program

Function list:

load_file(filename)
    - function to open a txt file and load the info into a list
    - parameters needed: filename(has to be a string)
    - return: list with string data from the txt file

'''
#================ Functions ===================

def load_file(filename):
    fileR = open(filename,"r")
    size = fileR.readline()
    size = int(size.strip())
    file_info = [None]*size
    for i in range(size):
        file_info[i] = fileR.readline().strip() 
    fileR.close()
    return file_info

#================= Main Program ==================