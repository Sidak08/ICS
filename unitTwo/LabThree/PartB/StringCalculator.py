'''
File: StringCalculator.py
Author: Sidak Singh
Date: Dec 4, 2024

Description:
    Takes in a string of 15 characters containing two numbers and one operator
    fulfills the operations and returns a string showing answer. The operator
    must be in the center

'''
def calc(inputStr: str) -> str:
    '''
    calc(inputString)
        - calculate the answer of the input string
        - parameters needed: inputStr(type: str):
            string of 15 characters containing two numbers and one operator
            operator must be in the center
        - return: type:str - string showing the answer or a error value
    '''
    try:
        num1 = float(inputStr[:7]) #find the first number
        num2 = float(inputStr[8:]) #find the second number
        answer = 0.0

        match (inputStr[7]):
            case "+": # performs addition
                answer = (num1 + num2)
            case "-": # performs susbtraction
                answer = (num1 - num2)
            case "x": # performs mutiplication
                answer = (num1 * num2)
            case "/": # performs division
                if num2 != 0.00: #checks if deviding by zero
                    answer = num1 / num2
                else:
                    answer = "undefined"
            case "%": # performs modulus
                if num2 != 0.00:
                    answer = num1 % num2 #checks if deviding by zero
                else:
                    answer = "undefined"

        if answer != "undefined": #formates the answer
            return "{:,.2f}".format(answer)
        else:
            return answer #returns if undefined
    except ValueError as valueError:
        #checks for value errors
        return f"Error Invalid Value: {str(valueError)}"
    except Exception as e:
        #checks for all errors
        return f"Unexpected error: {str(e)}"
