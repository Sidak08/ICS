'''
File: ConditionlStatements.y
Author Sidak Singh
Date: Nov 14, 2024

Description:
A review of if Else statements in python
'''

quit = False

while quit == False :
    choice = input("Choices: \n'I' to convert to inches\n'C' to conver to centimeters" +
        "\n'X' to exit\nEnter one of the choices abover ")

    if choice == "I":
        cm = float(input("\nEnter the value in cm: "))
        inches = cm / 2.54
        print(str(cm) + " cm is equaivalent to " + str(inches) + " inches")

    elif choice == "C":
        inches = float(input("\nEnter the value in inches: "))
        cm = inches * 2.54
        print(str(inches) + " inches is equaivalent to " + str(cm) + "cm")

    elif choice == "X":
        quit = True

print("Thank you, hope you enjoyed the experience")
