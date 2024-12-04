from ExpressionLoadPartC import loadFile, saveResults
from StringCalculator import calc
from tkinter import *
'''

File:PersonalInfoUI.py
Author: Dhenushan Ramesh
Date: Nov 27, 2024

Description:
The user interface for the Personal Information System Application

'''

try:
    fileName = input("Enter a file name: ")
    # fileName = "Questions.txt"
    inputData = loadFile(fileName)
    text = ""
    for i in range(len(inputData)):
        output = calc(inputData[i])
        text = text + f"{output}\n\n"
    print(text)
    saveResults(text)
    root = Tk()
    root.geometry("350x550")#set window size
    root.title("String Calulator")
    textOutput = Text(root, height=40, width=40)
    textOutput.grid(column=0, row=0, padx=50, pady=20)
    textOutput.insert(END, text)
    textOutput.config(state=DISABLED)
    root.mainloop()

except FileNotFoundError:
    print("\nError! " + fileName + " Not found")
except ValueError as e:
    print("\nError! " + fileName + " is corrupted")
    print(e)
