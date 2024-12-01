#Denu
from ExpressionLoad import load_file
from StringCalculator import calc
from tkinter import *
'''

File:PersonalInfoUI.py
Author: Dhenushan Ramesh
Date: Nov 27, 2024

Description:
The user interface for the Personal Infromation System Application

'''

try:
    file_name = input("Enter a file name: ")
    input_data = load_file(file_name)
    text = ""
    for i in range(len(input_data)):
        output = calc(input_data[i])
        text = text + output + "\n\n"   
    print(text)
    root = Tk()
    root.geometry("350x550")#set window size
    root.title("String Calulator")
    text_output = Text(root, height=40, width=40)
    text_output.grid(column=0, row=0, padx=50, pady=20)
    text_output.insert(END, text) 
    text_output.config(state=DISABLED)
    root.mainloop()

except FileNotFoundError:
    print("\nError! " + file_name + " Not found")
except ValueError as e:
    print("\nError! " + file_name + " is corrupted")
    print(e)