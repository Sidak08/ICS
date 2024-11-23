'''
File: ForLoopTest.py
Author: Sidak Singh
Date: Nov 13, 2024

Descripition:
Review on For loops.

'''
output = ""

for i in range(11):
    output = output + str(i) + " " # add i to
print(output)
output = ""

for i in range(11):
    if i == 5:
        continue
    output = output + str(i) + " "

print(output)
output = ""

for i in range(11):
    if i == 5:
        break
    output = output + str(i) + " "

print(output)
