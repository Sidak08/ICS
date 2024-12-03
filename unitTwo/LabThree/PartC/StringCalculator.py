from ast import Num


def calc(str: str) -> str:
    for i in range(1, len(str)):
        str = str.strip()
        match (str[i]):
            case "+":
                num1 = float(str[:i])
                num2 = float(str[i+1:])
                opp = float(str[i+1:])
                opp = str[i]
                answer = num1 + num2
                break
            case "-":
                num1 = float(str[:i])
                num2 = float(str[i+1:])
                opp = str[i]
                answer = num1 - num2
            case "x":
                num1 = float(str[:i])
                num2 = float(str[i+1:])
                opp = str[i]
                answer = num1 * num2
            case "/":
                num1 = float(str[:i])
                num2 = float(str[i+1:])
                opp = str[i]
                answer = num1 / num2
            case "%":
                num1 = float(str[:i])
                num2 = float(str[i+1:])
                opp = str[i]
                answer = num1 / num2

    return "{:,.2f} {} {:,.2f} = {:,.2f}".format(num1, opp, num2, answer)

print(calc("-003.00+0004.56"))
