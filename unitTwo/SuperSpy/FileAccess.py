'''
File: ExpressionLoadPartC.py
Author: Dhenushan Ramesh
Date: Dec 9, 2024

Description:
This program receives a file name from the EncryptionUI program and then opens
the specified text file, reads it, and then sends the info contained in it back to
the user Interface Program. It will also take the new information give from the EncryptionUI
and make it into a list and save to a new file.

Function list:
loadFile(filename)
    - function to open a txt file and load the info into a list
    - parameters needed: filename (has to be a string)
    - return: list with string data from the txt file

saveResults(fileInfo)
    - function to save results into a new file
    - parameters needed: fileInfo
    - return: does not return anything
'''

#================ Functions ===================

def load_file(file_name: str) -> list:
    '''
    Function to load the content of a text file into a list
    Parameters:
        file_name: The name of the file
    Returns:
        list: A list containing the lines of the file
    '''
    phrases = []  # Makes an empty list
    try:
        # Open the file in read mode
        fileR = open(file_name, "r")
        # Read the first line which tells the # of phrases, then removes
        # leading/trailing whitespace and convert it to an integer
        num_phrases = fileR.readline()
        num_phrases = int(num_phrases.strip())  
        # Loop through the number of phrases, read each line, Removes
        # leading/trailing whitespace and append it to the list
        for _ in range(num_phrases):
            line = fileR.readline()
            line = line.strip()
            phrases.append(line) 
        
    except FileNotFoundError as e:
        # Handle the case where the file is not found
        print(f"Error: File '{file_name}' not found.")
        print(e)
    
    return phrases  # Return the list of phrases

def save_to_file(filename: str, output_data: list) -> None:
    '''
    Function to save a list of phrases to a file.
    Parameters:
        filename (str): The name of the file to save to
        output_data : The list of phrases to write to the txt file 
    Returns: function does not return anything
    '''
    try:
        # Opens the file in write mode
        fileR = open(filename, "w")
        # Writes the number of phrases to the first line of the txt file
        fileR.write(str(len(output_data)) + "\n")
        # Write each phrase to the file, line by line to the txt file
        for phrase in output_data:
            fileR.write(phrase + "\n")
    except FileNotFoundError as e:
        # Add error handling when the file cannot be opened for writing
        print(f"Error: Could not open the file '{filename}' for writing.")
        print(e)


#------------- Main Program -------------------
if __name__ == "__main__":
    filename = input("What is the name of the file: ")
    phrases = load_file(filename)
    print(phrases)
    outputfile = input("Enter a output file name: ")
    save_to_file(outputfile, phrases)
    filename = input("What is filename") 
