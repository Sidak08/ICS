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

def load_file(file_name: str) -> list:
    phrases = []
    try:
        fileR = open(file_name,"r") 
        num_phrases = fileR.readline()
        num_phrases = int(num_phrases.strip())
        for _ in range(num_phrases):
            line = fileR.readline()
            line = line.strip()
            phrases.append(line)
    except FileNotFoundError as e:
        print(f"Error: File '{file_name}' not found.")
        print(e)
    return phrases

def save_to_file(filename: str, output_data: list) -> None:
    try:
        fileR = open(filename, "w")
        fileR.write(len(output_data))
        for phrase in output_data:
            fileR.write(phrase + "\n")
    except FileNotFoundError as e:
        print(f"Error: Could not open the file '{filename}' for writing.")
        print(e)


#------------- Main Program -------------------
filename = input("What is the name of the file: ")
phrases = load_file(filename)
print(phrases)
