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

def change_name():
    global name
    name ="John"

# --------------- Main Program -------------------------
name = input("Tell me your name: ")

say_happy()
say_happy()
greeting(name)
say_happy()

#step1
change_name()
greeting(name)
