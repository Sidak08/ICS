'''
File: StringCalculator.py
Author: Sidak Singh
Date: Dec 4, 2024

Description:
    Takes in a flexible string of max 20 characters containing two numbers and one
    operator fulfills the operations and returns a string showing the
    entire equations: number1 operator number2 = answer

'''
def calc(inputStr: str) -> str:
    '''
    calc(inputString)
        - calculate the answer of the input string
        - parameters needed: inputStr(type: str):
            string of 20 characters containing two numbers and one operator
        - return: type:str - string showing the entire equations or an error value:
            format: {number1} {operator} {number2} = {answer}
    '''
    try:
        for i in range(1, len(inputStr)): #loops the entire string
            inputStr = inputStr.strip() #removes extra space
            match (inputStr[i]): #find the opperation
                case "+": # performs addition
                    num1 = float(inputStr[:i])
                    num2 = float(inputStr[i + 1:])
                    opp = inputStr[i]
                    answer = num1 + num2
                    break
                case "-": # performs substraction
                    num1 = float(inputStr[:i])
                    num2 = float(inputStr[i+1:])
                    opp = inputStr[i]
                    answer = num1 - num2
                    break
                case "x": # performs mutiplication
                    num1 = float(inputStr[:i])
                    num2 = float(inputStr[i+1:])
                    opp = inputStr[i]
                    answer = num1 * num2
                    break
                case "/": # performs division
                    num1 = float(inputStr[:i])
                    num2 = float(inputStr[i+1:])
                    opp = inputStr[i]
                    if num2 != 0.00: #checks for division by zero
                        answer = num1 / num2
                    else:
                        answer = "undefined"
                    break
                case "%": # performs remainder
                    num1 = float(inputStr[:i])
                    num2 = float(inputStr[i+1:])
                    opp = inputStr[i]
                    if num2 != 0.00: #checks for remainder opperation by zero
                        answer = num1 % num2
                    else:
                        answer = "undefined"
                    break
        #formats the answer and returns it
        return  formatAnswer(num1, opp, num2, answer)
    except ValueError as valueError: #checks for value errors
        return f"Error Invalid Value: {str(valueError)}"
    except Exception as e: #checks for any errors
        return f"Unexpected error: {str(e)}"

def formatAnswer(num1, opp, num2, answer):
    '''
    formatAnswer(num1, opp, num2, answer)
        - formats the values into a equation with 2 decimal places
        - parameters needed:
            num1 = type:float - the first number of the equation
            opp = type:str - the opperation being performed
            num2 = type:float - the second number of the equation
            answer = type:float - answer to the eqation
        - return: type:str - string showing the entire equations:
            format: {number1} {operator} {number2} = {answer}
    '''
    if answer != "undefined": #checks if the answer is undfined
        return "{:,.2f} {} {:,.2f} = {:,.2f}".format(num1, opp, num2, answer)
    else: #returns formatted answer
        return "{:,.2f} {} {:,.2f} = {}".format(num1, opp, num2, answer)
