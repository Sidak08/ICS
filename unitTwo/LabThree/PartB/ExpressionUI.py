from ExpressionLoad import loadFile
from StringCalculator import calc
from tkinter import *
'''

File:PersonalInfoUI.py
Author: Dhenushan Ramesh
Date: Nov 27, 2024

Description:
The user interface for the stringcalculator

'''

try:
    fileName = input("Enter a file name: ")  # ask the user for a file name
    inputData = loadFile(fileName)  # Calls the loadFile function
    text = ""  # makes an empty string to store output
    for i in range(len(inputData)):  # look through entire list
        output = calc(inputData[i])  # calls the calc function
        text = text + f"{output}\n"  # makes the new output with proper format
    
    root = Tk()  # makes a Tkinter window
    root.geometry("350x550")  # Set window size to 350x550 
    root.title("String Calculator")  # makes the window title to "String Calculator"
    textOutput = Text(root, height=40, width=40) # Create a text widget for displaying the output
    textOutput.grid(column=0, row=0, padx=50, pady=20)  # position for text widget
    textOutput.insert(END, text)  # Puts output in text widget
    textOutput.config(state=DISABLED)  # stop editing for the user
    root.mainloop()  # activates the tkinter

except FileNotFoundError:
    print("\nError! " + fileName + " Not found")  # Print an error message if the file is not found
except ValueError as e:
    print("\nError! " + fileName + " is corrupted")  # Print an error message if the file is corrupted
    print(e)  # prints the specific problem

