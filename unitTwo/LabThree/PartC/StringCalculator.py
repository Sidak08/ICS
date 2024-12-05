'''
File: Loader.py
Author: Dhenushan Ramesh
Date: Nov 30, 2024

Description:
This program recives a file name from the User Interface program and then opens
the specified text file, reads it and then send the info contained in it back to
the user Interface Program
'''
def calc(str: str) -> str:
    '''
    Calc(filename)
        - function to open a txt file and load the info into a list
        - parameters needed: filename(has to be a string)
        - return: list with string data from the txt file
    '''
    print("inp", str)
    for i in range(1, len(str)):
        str = str.strip()
        match (str[i]):
            case "+":
                num1 = float(str[:i])
                num2 = float(str[i + 1:])
                opp = str[i]
                answer = num1 + num2
                break
            case "-":
                num1 = float(str[:i])
                num2 = float(str[i+1:])
                opp = str[i]
                answer = num1 - num2
                break
            case "x":
                num1 = float(str[:i])
                num2 = float(str[i+1:])
                opp = str[i]
                answer = num1 * num2
                break
            case "/":
                num1 = float(str[:i])
                num2 = float(str[i+1:])
                opp = str[i]
                if num2 != 0.00:
                    answer = num1 / num2
                else:
                    answer = "undefined"
                break
            case "%":
                num1 = float(str[:i])
                num2 = float(str[i+1:])
                opp = str[i]
                if num2 != 0.00:
                    answer = num1 / num2
                else:
                    answer = "undefined"
                break
    return  formatAnswer(num1, opp, num2, answer)

def formatAnswer(num1, opp, num2, answer):
    if answer != "undefined":
        return "{:,.2f} {} {:,.2f} = {:,.2f}".format(num1, opp, num2, answer)
    else:
        return "{:,.2f} {} {:,.2f} = {}".format(num1, opp, num2, answer)
