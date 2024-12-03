from Loader import loadFile
from Processor import proccesInfo
from tkinter import *
'''
File: PersonalInfoUi.py
Author: Sidak Singh
Date: Nov 27, 2024

Description:
the user interface for the personal information program
'''
try:
    # fileName = input("Enter the name of the file: ")
    fileName = "PersonalsInfoFile.txt"

    inputData = loadFile(fileName)

    text = ""

    for i in range(len(inputData)):
        output = proccesInfo(inputData[i])
        text = text + output + "\n\n"

    print(text)

    root = Tk()
    root.geometry("350x550")
    root.title("Personal Information System")

    text_output = Text(root, height=30, width=30)
    text_output.grid(column=0, row=0, padx=50, pady=20)
    text_output.insert(END, text)
    text_output.config(state=DISABLED)

    root.mainloop()

except FileNotFoundError:
    print(f"Error! {fileName} Not Found")

except ValueError as e:
    print(f"\n Error! {fileName} is corupt")
    print(e)

except Exception as e:
    print(e)
