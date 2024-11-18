'''
File: LabOneMerryChristmas.py
Author: Sidak Singh
Date: Nov 15 2024

Description:
Uses multiple functions to create a song used to wish you Christmas.

Function List:
    wishYouChristmas
        Prints:
            "We wish {name} a merry Christmas" 3 times
            "And a happy New Year!" 1 time
        Parameter:
            Takes in "name" as argument. "you" is the default value.
        Return:
            No return

    gladTidingsBringNewYear
        Prints:
            "Glad tidings we bring\nTo you and your kin\n"
            "Glad tidings for Christmas\nAnd a happy New Year!"
        Parameters:
            No Parameters
        Return:
            No return

    figgyPudding
        Prints:
            "We want some figgy pudding" 3 times
            "Please bring it right here!" 1 time
        Parameters:
            No Parameters
        Return:
            No return

    printSong
        Prints:
            Prints the entire song
        Parameters:
            Takes in (name) as argument. (you) is the default value.
        Return:
            No return
'''

#========================== Functions ======================================
def wishYouChristmas(name = "you"):
    for i in range(3):
        print(f"We wish {name} a merry Christmas")
    print("And a happy New Year!")

def gladTidingsBringNewYear():
    print('''Glad tidings we bring\nTo you and your kin\nGlad \
tidings for Christmas\nAnd a happy New Year!''')

def figgyPudding():
    for i in range(3):
        print("We want some figgy pudding")
    print("Please bring it right here!")

def printSong(name = "you"):
    wishYouChristmas(name)
    gladTidingsBringNewYear()
    figgyPudding()
    gladTidingsBringNewYear()
    figgyPudding()
    gladTidingsBringNewYear()
    wishYouChristmas(name)
    gladTidingsBringNewYear()

#========================== Main program ===================================
name = input("What is your name: ")
printSong(name)
