from tkinter import *
'''
File: HappyBirthday.py
Author: Sidak Singh
Date: November 5th, 2024

Description:
This program displays the Happy Birthday song using a custom function.

Function List:

say_happy(name):
    - prints the phrase "Happy Birthday to you"
    - parameters needed: name
    - nothing to return
greeting(name)
  - prints custom greeting with a name
  - parameter needed: string name
  - nothing returned
'''

#--------------- Define custom function ---------------
def say_happy():
    print("Happy Birthday to you")
def greeting(name: str):
    print("Happy Birthday to you dear " + name)

def okClicked():
    pass

# def change_name():
#     global name
#     name ="John"

# --------------- Main Program -------------------------
# name = input("Tell me your name: ")
# say_happy()
# say_happy()
# greeting(name)
# say_happy()

# #step1
# change_name()
# greeting(name)

#Create and root window and set size
root = Tk()
root.geometry("440x180")
root.title("Happy Birthday Application")

#create and place a label to promt user for a name
nameLable = Label(root, text="Enter your name: ")
nameLable.grid(column=0, row=0)

# create user entry
inputBox = Entry(root, width=15)
inputBox.grid(column=1, row=0)

#create and place a button
okButton = Button(root, text="OK", command= okClicked)
okButton.grid(column=0, row=1, columnspan=2)

root.mainloop()
