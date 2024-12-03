#Sidak
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

print(calc("-003.00+0004.56"))
