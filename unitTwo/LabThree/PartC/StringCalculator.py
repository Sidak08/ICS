def calc(str: str) -> str:
    print(str)
    for i in range(1, len(str)):
        str = str.strip()
        match (str[i]):
            case "+":
                num1 = float(str[:i - 1])
                num2 = float(str[i:])
                opp = str[i]
                answer = num1 + num2
                break
            case "-":
                num1 = float(str[:i - 1])
                num2 = float(str[i+1:])
                opp = str[i]
                answer = num1 - num2
                # print("num1:", num1, "num2", num2, "opp:", opp)
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
                answer = num1 / num2
                break
            case "%":
                num1 = float(str[:i])
                num2 = float(str[i+1:])
                opp = str[i]
                answer = num1 / num2
                break


    return "{:,.2f} {} {:,.2f} = {:,.2f}".format(num1, opp, num2, answer)

print(calc("-003.00--0004.56"))
