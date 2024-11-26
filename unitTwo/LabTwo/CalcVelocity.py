'''
File: CalcVelocity.py
Author: Sidak Singh
Date: Nov 21 2024

Description: Finds the final velocity of an object in km/s and m/s using its
height and initial velocity.

Function List:
    calcVelocity:
        does:
            calculates the final velocity of an object
        parameters:
            The (initialVelocity) in m/s and (height) in m
        returns:
            Gives the final velocity of an object in m/s
    convertMetersPerSecToKilometersPerHour:
        does:
            converts the velocity from m/s to km/h
        parameters:
            metersPerSec
        returns:
            metersPerSec converted to km/h
'''

def calcVelocity(initialVelocity, height):
    global GRAVITY
    return (initialVelocity**2 + 2 * GRAVITY * height)**0.5

def convertMetersPerSecToKilometersPerHour(metersPerSec):
    return metersPerSec * 3.6

GRAVITY = 9.8

while True:
    height = float(input("Enter the height of the object in meters: "))
    initialVelocity = float(input("Enter the initial velocity of the object in m/s: "))

    finalVelocityInMeters = calcVelocity(initialVelocity, height)
    finalVelocityInKilometers = convertMetersPerSecToKilometersPerHour(finalVelocityInMeters)

    print("The final velocity of the object is {:.2f} m/s\n"
          "or {:.2f} km/h.".format(finalVelocityInMeters, finalVelocityInKilometers))

    choice = input("Press 'q' to quit or 'c' to continue: ")
    if choice == "q":
        break
