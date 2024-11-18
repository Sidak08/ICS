'''
File: SpeedCalculation.py
Author: Sidak Singh
Date: Nov 18, 2024

Description:
Allows user to enter the distance and time for any object and calculate
the average speed using the following formula

speed = distance / time

Function List:
    calcSpeed(dist, time):
        -Calculates the speed based on distance and time
        -pramters requires: distance(float) in meters, time(float) in seconds
        -return speed(float)
'''
#========================== Functions ======================================
def calcSpeed(dist, time):
    return dist/time

#========================== Main program ===================================
#create list
dist = [0.0] * 3
time = [0.0] * 3
speed = [0.0] * 3

for i in range(len(dist)):
    #promt user to input the distance
    dist[i] = float(input("Enter the distance traveled in meter: "))

    #promt and get time from user
    time[i] = float(input("enter the time in seconds: "))

    #calc the speed and display it
    speed[i] = calcSpeed(dist[i], time[i])
    print(f"The average speed is {speed[i]} m/s")
