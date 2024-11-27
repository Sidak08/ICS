'''
File: Procersor.py
Author: Sidak Singh
Date: Nov 25, 2024

Description: This program converts the raw string into a proper string
'''

def proccesInfo(myWord):
    '''
    Takes a string containing the first name, last name, age, and splits them
    into the correct formate

    Parameters:
        myString(str) - input string containing the first name, last name, age, and gender

    Returns:
        formattedInfo(str) - the formatted string
    '''
    myWord = myWord.split()

    for i in range(len(myWord)):
        match i:
            case 0:
                firstName = myWord[i]
            case 1:
                lastName = myWord[i]
            case 2:
                age = int(myWord[i])
            case 3:
                gender = myWord[i]

    genderType = formateGender(gender)

    formattedInfo = ("Last Name:\t\t" + lastName + "\n" + "First Name:\t\t" +
        firstName + "\n" + "Age:\t\t" + str(age) + "\nGender: \t\t" + genderType)

    return formattedInfo

def formateGender(gender):
    '''
    Takes a letter represnting gender and converts ot a work

    Paramters:
        gender(str) - letter representing gender

    Returns:
        genderStr(str) - gender as a word
    '''
    genderStr = "Other"
    match gender:
        case "m":
            genderStr = "Male"
        case "f":
            genderStr = "Female"
        case _:
            genderStr = "Other"
    return genderStr


#=============================Main Program=====================================
if __name__ == "__main__":
    print(proccesInfo("Singh Sidak 20 m"))
    inputList = [None] * 3
    outputList = [None] * 3

    inputList[0] = "Singh Sidak 20 m"
    inputList[1] = "Dath Karam 25 f"
    inputList[2] = "Kaur Simran 22 ?"

    for i in range(len(inputList)):
        outputList[i] = proccesInfo(inputList[i])
        print(outputList[i])
