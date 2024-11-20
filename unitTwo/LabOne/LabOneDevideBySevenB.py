'''
File: LabOneDevideBySevenB.py
Author: Sidak Singh
Date: Nov 15 2024

Description: Displays the sum and all the numbers from 3 to 47 that are divisible
by 7 using an infinite while loop
'''

#========================== Main program ===================================
sum = 0
i = 3
print("All the numbers between 3 and 47 which are divisible 7")

while(True):
    if (i == 47):
        break
    if (i % 7 == 0):
        print(i)
        sum += i
    i+= 1

print(f"The sum of all of these numbers is {sum}")
