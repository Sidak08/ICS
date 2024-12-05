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
    inputData = loadFile(fileName)
    text = ""
    for i in range(len(inputData)):
        output = calc(inputData[i])
        text = text + f"{output}\n"
    saveResults(text)
    root = Tk()
    root.geometry("450x550")#set window size
    root.title("String Calulator")
    textOutput = Text(root, height=80, width=80)
    textOutput.grid(column=0, row=0, padx=50, pady=20)
    textOutput.insert(END, text)
    textOutput.config(state=DISABLED)
    root.mainloop()

except FileNotFoundError:
    print("\nError! " + fileName + " Not found")
except ValueError as e:
    print("\nError! " + fileName + " is corrupted")
    print(e)
