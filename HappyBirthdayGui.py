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
def sayHappy():
    global output
    output += "Happy Birthday to you\n"
def greeting(name: str):
    global output
    output += "Happy Birthday to you dear " + name + "\n"
def okClicked():
    global textOutput
    name = inputBox.get()

    output = ""
    sayHappy()
    sayHappy()
    greeting(name)
    sayHappy()
    textOutput.delete("1.0", END)
    textOutput.insert(END, output)


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

output = ""

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
okButton = Button(root, text="OK", command=okClicked)
okButton.grid(column=0, row=1, columnspan=2)

#create text widget and its size
textOutput = Text(root, width=35, height=5)
textOutput.grid(column=0, row=2, columnspan=2)
textOutput.config(state=NORMAL)
textOutput.insert(END, "")
textOutput.config(state=DISABLED)


#insert the happyBirthday photo
cakeImg = PhotoImage(file="cake.png")
cakeImgLabel = Label(root, image=cakeImg)
cakeImgLabel.grid(column=2, row=0, rowspan=3)

root.mainloop()
