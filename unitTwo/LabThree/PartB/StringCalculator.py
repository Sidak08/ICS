'''
File:StringCalculator.py
Author: Sidak Singh
Date: Nov 27, 2024

Description:
The user interface for the Personal Information System Application
'''
def calc(str: str) -> float:
    num1 = float(str[:7])
    num2 = float(str[8:])
    answer = 0.0

    match (str[7]):
        case "+":
           answer = (num1 + num2)
        case "-":
            answer = (num1 - num2)
        case "x":
            answer = (num1 * num2)
        case "/":
            answer = (num1 / num2)
        case "%":
            answer = (num1 % num2)

    return round(answer, 2)
